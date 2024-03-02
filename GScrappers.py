import re
import os
import requests
import pandas as pd
from urllib.parse import unquote
from bs4 import BeautifulSoup
from Google_Parameters import google_params


class GScrappers():
    ###############################################################################################################################################################################################################
    ######################################################################################### Google Functions ####################################################################################################
    ###############################################################################################################################################################################################################
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Function 1 : Google Advanced URL Builder
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Google_Advanced_URL(main_query, search_type='', exact_words='', any_of_words='', none_of_words='',number_from='', number_to='', site_or_domain='', results_count='',
                            start_date='', end_date='', search_language='English', country='', term_apperaing='', file_type=''):

        # Building Main Query
        MAIN_QUERY = f"&as_q={main_query}".replace(" ","+")
        exact_words = '+OR+'.join(['"' + word + '"' for word in exact_words])  if exact_words else ''
        EXACT_WORDS = f"&as_epq={exact_words}" if exact_words else ''
        ANY_OF_WORDS = f"&as_oq={any_of_words}" if any_of_words else ''
        none_of_words = "+".join(none_of_words) if none_of_words else ''
        NONE_OF_WORDS = f"&as_eq={none_of_words}" if none_of_words else ''
        NUMBER_FROM = f"&as_nlo={number_from}" if number_from else ''
        NUMBER_TO = f"&as_nhi={number_to}" if number_to else ''
        SITE_OR_DOMAIN = f"&as_sitesearch={site_or_domain}" if site_or_domain else ''
        RESULTS_COUNTS = f"&num={int(results_count)}" if results_count else ''
        DATE = f"&tbs=cdr:1,cd_min:{start_date},cd_max:{end_date}" if start_date or end_date else ''
        SEARCH_TYPE = google_params.search_type()[search_type] if search_type else ''
        LANGUGAGE = google_params.languages()[search_language] if search_language else ''
        COUNTRY = google_params.countries()[country] if country else ''
        TERM_APPERAING = google_params.term_apperaing()[term_apperaing] if term_apperaing else ''
        FILE_TYPE = google_params.file_type()[file_type] if file_type else ''
        
        # Building Final Search URL
        if search_type != 'Scholar':
            Url = f"https://www.google.com/search?{MAIN_QUERY}{EXACT_WORDS}{ANY_OF_WORDS}{NONE_OF_WORDS}{NUMBER_FROM}{NUMBER_TO}{SITE_OR_DOMAIN}{RESULTS_COUNTS}{DATE}{SEARCH_TYPE}{LANGUGAGE}{COUNTRY}{TERM_APPERAING}{FILE_TYPE}"
        else:
            Url = f"https://scholar.google.com/scholar?&{MAIN_QUERY}{EXACT_WORDS}{ANY_OF_WORDS}{NONE_OF_WORDS}{NUMBER_FROM}{NUMBER_TO}{SITE_OR_DOMAIN}{RESULTS_COUNTS}{DATE}{LANGUGAGE}{COUNTRY}{TERM_APPERAING}{FILE_TYPE}"
        
        # Return URL
        return Url
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Function 2 : Google News Extractor
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Google_Results(Search_URLS,Search_Type=''):
        response = requests.get(Search_URLS)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.content,'html.parser')

        Results = [a for a in soup.find_all("a", href=True) if 'data-ved' in a.attrs]
        Final_Results = []
        
        
        # Extarct From Google News
        if Search_Type == 'News':
            for result in Results:
                Headline = result.find('h3').text
                Date = result.find(class_="r0bn4c rQMQod").text
                Link = unquote(result.attrs['href'].split("/url?q=")[1].split('&sa')[0])

                page = {"Headline":Headline,
                        "Date":Date,
                        "Link":Link}
                
                Final_Results.append(page)
                
                
        # Extarct From Open Search      
        else:
            for result in Results:
                try:
                    Headline = result.find('h3').text
                    Link = unquote(result.attrs['href'].split("/url?q=")[1].split('&sa')[0])

                    page = {"Headline":Headline,
                            "Link":Link}
                
                    Final_Results.append(page)
                except:
                    pass
            
        Google_Results = pd.DataFrame(Final_Results).drop_duplicates(subset=['Link'])
        
        return Google_Results
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




    ###############################################################################################################################################################################################################
    ######################################################################################### Scrapping Functions #################################################################################################
    ###############################################################################################################################################################################################################
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Function 3 : Website Scrapper
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Website_Scraper(URL,Keywords=''):
        try:
            #--------------------------------------------------------------------------------
            # Step 1: Get Page Content
            #--------------------------------------------------------------------------------
            HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
            response = requests.get(URL, headers=HEADERS, timeout=60)
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.text,"html.parser")
                except:
                    soup = BeautifulSoup(response.text,"html5lib")


            
            #--------------------------------------------------------------------------------
            # Step 2: Get Page Paragraphs
            #--------------------------------------------------------------------------------
            Paragraphs = []
            body_text = soup.find_all('p')
            
            for entry in body_text:
            #    if len(entry.text) > 1:
                p = f"({body_text.index(entry)})" + " • " + entry.text.strip().title() + '\n'
                if p not in Paragraphs:
                    Paragraphs.append(p)
                        
            #--------------------------------------------------------------------------------
            # Step 3: Get Most Relevant Paragraphs
            #--------------------------------------------------------------------------------
            Most_Relevant_Paragraphs = []
            if len(Keywords) != 0:
                for keyword in Keywords:
                    for paragraph in Paragraphs:
                        if paragraph.lower() not in Most_Relevant_Paragraphs:
                            if keyword.lower() in paragraph.lower():
                                Most_Relevant_Paragraphs.append(paragraph)
                        else:
                            pass
                Most_Relevant_Paragraphs = "\n".join(Most_Relevant_Paragraphs)
            else:
                Most_Relevant_Paragraphs = ""
            
            #--------------------------------------------------------------------------------
            # Step 4: Keyword Analysis
            #--------------------------------------------------------------------------------
            Keywords_Analysis = []
            Keywords_Totals = 0
            if len(Keywords) > 0: 
                for keyword in Keywords:
                    keyword_count = "\n".join(Paragraphs).lower().count(keyword.lower())
                    Keywords_Totals = Keywords_Totals + keyword_count
                    Keywords_Analysis.append(" • " + keyword.title() + " : " + str(keyword_count))
            """          
            #--------------------------------------------------------------------------------
            #################################################################################
            # Step 5: AI Summarization
            ### TO BE COMPLETED IN FUTURE ###
            #################################################################################
            """
            #--------------------------------------------------------------------------------
            # Step 6: Create DF entry
            page = {
                    "Paragraphs":"\n".join(Paragraphs),
                    "Most Relevant Paragraphs":Most_Relevant_Paragraphs,
                    "Keywords Analysis":"\n".join(Keywords_Analysis),
                    "Keywords Total":Keywords_Totals,
                    "Link":URL}
   
            #--------------------------------------------------------------------------------
            
        except Exception as e:
            print(f'Error Faced in Web Content Scrapping: \n{e}')
            page = {
                "Paragraphs":"Site Wasn't Scrapped",
                "Most Relevant Paragraphs":"Site Wasn't Scrapped",
                "Keywords Analysis":"Site Wasn't Scrapped",
                "Keywords Total":"Site Wasn't Scrapped",
                "Link":URL}
            pass
                        
        return page 
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    ###############################################################################################################################################################################################################
    ######################################################################################### Suppport Functions ##################################################################################################
    ############################################################################################################################################################################################################### 
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Function 1 : Results Formating
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Result_Formating(Google_Results,Scrapping_Results,Keywords=''):
        # Merge Dataframes
        Final_Results = pd.merge(Google_Results,Scrapping_Results,on='Link')
        
        # Drop Duplicates and Empty Columns
        Final_Results = Final_Results.drop_duplicates(subset='Link').dropna(axis=1, how='all')
        
        # Calculate Relevancy Score
        try:
            Final_Results['Keywords Total'] = pd.to_numeric(Final_Results['Keywords Total'], errors='coerce')
            Total_Keywords = Final_Results['Keywords Total'].sum()
            Final_Results['Relevancy Score'] = Final_Results['Keywords Total'] / Total_Keywords
        except:
            Total_Keywords = 0
            Final_Results['Relevancy Score'] = 0
            
        #Rearrange collumns
        if len(Keywords) != 0:
            try:
                Final_Results = Final_Results[['Headline', 'Date', 'Paragraphs', 'Most Relevant Paragraphs', 'Keywords Analysis', 'Keywords Total', 'Relevancy Score', 'Link']]
            except:
                Final_Results = Final_Results[['Headline', 'Paragraphs', 'Most Relevant Paragraphs', 'Keywords Analysis', 'Keywords Total', 'Relevancy Score', 'Link']]
            # Sort by Keywords Total
            Final_Results = Final_Results.sort_values(by='Relevancy Score',ascending=False)
            Final_Results = Final_Results.reset_index(drop=True)
        
        else:
            try:
                Final_Results = Final_Results[['Headline', 'Date', 'Paragraphs', 'Link']]
            except:
                Final_Results = Final_Results[['Headline', 'Paragraphs', 'Link']]
                
        return Final_Results
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
