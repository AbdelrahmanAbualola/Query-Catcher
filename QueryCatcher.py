import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
from time import sleep
from stqdm import stqdm
from GScrappers import *
from Google_Parameters import *
import pandas as pd
from datetime import datetime, timedelta
import xlsxwriter
import io

###############################################################################################################################################################################################################
# User Inputs
###############################################################################################################################################################################################################
st.title('Welcome to :blue[Query Catcher]')
st.markdown('This tool has been developed for quick research and website scrapping')
st.subheader('Start your Search',divider='rainbow')

Search_Type = st.radio('Search Type',pd.DataFrame(list({'Simple Search':1,'Advanced Search':2})),horizontal=True)
Search_Query= st.text_input('Search Query')
Search_Source = st.radio('Search Source',pd.DataFrame(list(google_params.search_type_basic())),horizontal=True)

if Search_Type == 'Advanced Search': st.divider()

Included_Keywords = st_tags(label='Included Keywords:', text='Press enter to add more', maxtags = 100, key='Included Keywords') if Search_Type == 'Advanced Search' else ""
Discarded_Keywords= st_tags(label='Discarded Keywords:', text='Press enter to add more', maxtags = 100, key='Discarded Keywords') if Search_Type == 'Advanced Search' else ""

if Search_Type == 'Advanced Search': st.divider()

col1, col2 = st.columns(2)
with col1:
    Terms_Appearing = st.selectbox('Keywords Apeearning',google_params.term_apperaing().keys(),placeholder="Choose a Country") if Search_Type == 'Advanced Search' else ""
    Country = st.selectbox('Country',google_params.countries().keys(),placeholder="Choose a Country") if Search_Type == 'Advanced Search' else ""
    Language = st.selectbox('Language',google_params.languages().keys(),placeholder="Choose a search language") if Search_Type == 'Advanced Search' else ""

with col2:
    Date_Range = st.date_input ('Date Range',value=[],format="DD/MM/YYYY",help='Select start and end date for the search') if Search_Type == 'Advanced Search' else ""
    Results_Quantity = st.number_input('Results Quantity',min_value=10,max_value=100) if Search_Type == 'Advanced Search' else ""

Session = st.session_state

###############################################################################################################################################################################################################
# Extraction
###############################################################################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section 1: Get Gogogle Results
st.divider()
col3,col4,col5,col6 = st.columns(4)

with col3:
    Start_Search = st.button ('Start Search')
if Start_Search:
    # Step 1: Prepare Search URL
    Start_Date = Date_Range[0].strftime("%m-%d-%Y") if Search_Type == 'Advanced Search' else ""
    End_Date = Date_Range[1].strftime("%m-%d-%Y")  if Search_Type == 'Advanced Search' else ""
    Google_URL = GScrappers.Google_Advanced_URL(Search_Query, search_type=Search_Source, exact_words=Included_Keywords, any_of_words='', none_of_words=Discarded_Keywords,
                                                number_from='', number_to='', site_or_domain='', results_count=Results_Quantity,
                                                start_date=Start_Date, end_date=End_Date, search_language=Language, country=Country, term_apperaing=Terms_Appearing, file_type='')
    st.write(f"Search started at: [link]({Google_URL})")
    # Step 2: Get Google Search Results
    Google_Results = GScrappers.Google_Results(Google_URL,Search_Source)
    
    st.subheader('Search Results',divider='rainbow')
    st.data_editor(Google_Results,column_config={"Link":st.column_config.LinkColumn("Source",display_text='Link')},width=1280)
    
    # Step 3: Save results to Session
    st.session_state['google_results'] = Google_Results
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section 2: Scrape Google Results
if 'google_results' in Session.keys():
    
    # Step 1: Ask if User want to scrape
    with col4:
        Start_Scapping = st.button('Start Scapping')
    if Start_Scapping:
        # Get Links from Google Results
        Links = Session['google_results']['Link']
        
        # Itterate over each link to scrape website and save in Scrapped_Websites_List
        Scraped_Websites_List = []
        for link in stqdm(Links):
            Website_dict = GScrappers.Website_Scraper(link,Included_Keywords)
            Scraped_Websites_List.append(Website_dict)
        
        # Create a Dataframe for scrapping results and save in Session   
        Scraped_Websites_DF = pd.DataFrame(Scraped_Websites_List)
        Session['Scraped_Websites_DF'] = Scraped_Websites_DF
        
        # Merge Scraped Websites with Google Results and Format the findings
        Final_Results = GScrappers.Result_Formating(Session['google_results'],Scraped_Websites_DF,Included_Keywords)
        
        st.subheader('Scrapping Results',divider='rainbow')
        st.data_editor(Final_Results,column_config={"Link":st.column_config.LinkColumn("Source",display_text='Link')})
        Session['Final_Results'] = Final_Results
        

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if 'Final_Results' in Session.keys():
        
    with col5:
        buffer = io.BytesIO()
        df = Session['Final_Results']
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet.
            df.to_excel(writer, sheet_name='Sheet1', index=False)

        Donwload = st.download_button('Download Results',data=buffer,file_name="Results.xlsx",mime='textcsv')
        
    with col6:
        Refresh = st.button('Reset Research')
        if Refresh:
            for key in Session.keys():
                del Session[key]
