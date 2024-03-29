class google_params:
    ##########################################################################################################################################################################################################
    def query_keys():
        query_keys_dict = {
                '': '',
                'main_query': 'as_q=',
                'exact_word': '&as_epq=',
                'any_of_words': '&as_oq=',
                'none_of_words': '&as_eq=',
                'number_from': '&as_nlo=',
                'number_to': '&as_nhi=',
                'site_or_domain': '&as_sitesearch=',
                'results_count': '&num='}
               
        return query_keys_dict
    ##########################################################################################################################################################################################################
    
    
    ##########################################################################################################################################################################################################   
    def query_date(start_date='',end_date=''):
        param = f"&tbs=cdr:1,cd_min:{start_date},cd_max:{end_date}"
        return param
    ##########################################################################################################################################################################################################
    
    
    
    ##########################################################################################################################################################################################################
    def search_type():
        search_types_dict = {
            'Open Search':'',
            'Applications': '&tbm=app',
            'Blogs': '&tbm=blg',
            'Books': '&tbm=bks',
            'Discussions': '&tbm=dsc',
            'Images': '&tbm=isch',
            'News': '&tbm=nws',
            'Patents': '&tbm=pts',
            'Places': '&tbm=plcs',
            'Recipes': '&tbm=rcp',
            'Shopping': '&tbm=shop',
            'Video': '&tbm=vid',
            'Scholar' : 'https://scholar.google.com/scholar?' }

        return search_types_dict
    ##########################################################################################################################################################################################################    
    
    
    ##########################################################################################################################################################################################################
    def search_type_basic():
        search_types_dict = {
            'Open Search':'',
            'News': '&tbm=nws'
            }
        return search_types_dict    
    ##########################################################################################################################################################################################################
    
    
    
    ##########################################################################################################################################################################################################
    def languages():
        langs_dict = {
                    'Language': '',
                    'Arabic': '&lr=lang_ar',
                    'Armenian': '&lr=lang_hy',
                    'Belarusian': '&lr=lang_be',
                    'Bulgarian': '&lr=lang_bg',
                    'Catalan': '&lr=lang_ca',
                    'Croatian': '&lr=lang_hr',
                    'Czech': '&lr=lang_cs',
                    'Danish': '&lr=lang_da',
                    'Dutch': '&lr=lang_nl',
                    'English': '&lr=lang_en',
                    'Esperanto': '&lr=lang_eo',
                    'Estonian': '&lr=lang_et',
                    'Filipino': '&lr=lang_tl',
                    'Finnish': '&lr=lang_fi',
                    'French': '&lr=lang_fr',
                    'German': '&lr=lang_de',
                    'Greek': '&lr=lang_el',
                    'Hebrew': '&lr=lang_iw',
                    'Hungarian': '&lr=lang_hu',
                    'Icelandic': '&lr=lang_is',
                    'Indonesian': '&lr=lang_id',
                    'Italian': '&lr=lang_it',
                    'Japanese': '&lr=lang_ja',
                    'Korean': '&lr=lang_ko',
                    'Latvian': '&lr=lang_lv',
                    'Lithuanian': '&lr=lang_lt',
                    'Norwegian': '&lr=lang_no',
                    'Persian': '&lr=lang_fa',
                    'Polish': '&lr=lang_pl',
                    'Portuguese': '&lr=lang_pt',
                    'Romanian': '&lr=lang_ro',
                    'Russian': '&lr=lang_ru',
                    'Serbian': '&lr=lang_sr',
                    'Slovak': '&lr=lang_sk',
                    'Slovenian': '&lr=lang_sl',
                    'Spanish': '&lr=lang_es',
                    'Swedish': '&lr=lang_sv',
                    'Thai': '&lr=lang_th',
                    'Turkish': '&lr=lang_tr',
                    'Ukrainian': '&lr=lang_uk',
                    'Vietnamese': '&lr=lang_vi',
                    'Chinese Simplified': '&lr=lang_zh-CN',
                    'Chinese Traditional': '&lr=lang_zh-TW'}       
        
        return langs_dict
    ##########################################################################################################################################################################################################
    
    
    
    ##########################################################################################################################################################################################################
    def interface_langs():
        interface_langs_dict = {
                'English': 'hl=en',
                'Arabic': 'hl=ar',
                'Armenian': 'hl=hy',
                'Belarusian': 'hl=be',
                'Bulgarian': 'hl=bg',
                'Catalan': 'hl=ca',
                'Croatian': 'hl=hr',
                'Czech': 'hl=cs',
                'Danish': 'hl=da',
                'Dutch': 'hl=nl',
                'Esperanto': 'hl=eo',
                'Estonian': 'hl=et',
                'Filipino': 'hl=tl',
                'Finnish': 'hl=fi',
                'French': 'hl=fr',
                'German': 'hl=de',
                'Greek': 'hl=el',
                'Hebrew': 'hl=iw',
                'Hungarian': 'hl=hu',
                'Icelandic': 'hl=is',
                'Indonesian': 'hl=id',
                'Italian': 'hl=it',
                'Japanese': 'hl=ja',
                'Korean': 'hl=ko',
                'Latvian': 'hl=lv',
                'Lithuanian': 'hl=lt',
                'Norwegian': 'hl=no',
                'Persian': 'hl=fa',
                'Polish': 'hl=pl',
                'Portuguese': 'hl=pt',
                'Romanian': 'hl=ro',
                'Russian': 'hl=ru',
                'Serbian': 'hl=sr',
                'Slovak': 'hl=sk',
                'Slovenian': 'hl=sl',
                'Spanish': 'hl=es',
                'Swedish': 'hl=sv',
                'Thai': 'hl=th',
                'Turkish': 'hl=tr',
                'Ukrainian': 'hl=uk',
                'Vietnamese': 'hl=vi',
                'Chinese Simplified': 'hl=zh-CN',
                'Chinese Traditional': 'hl=zh-TW'}
        return interface_langs_dict
    ##########################################################################################################################################################################################################    
        
        
        
    ##########################################################################################################################################################################################################
    def countries():
        countries_dict = {'Country':'',
                    'Afghanistan': '&cr=countryAF',
                    'Albania': '&cr=countryAL',
                    'Algeria': '&cr=countryDZ',
                    'American Samoa': '&cr=countryAS',
                    'Andorra': '&cr=countryAD',
                    'Angola': '&cr=countryAO',
                    'Anguilla': '&cr=countryAI',
                    'Antarctica': '&cr=countryAQ',
                    'Antigua and Barbuda': '&cr=countryAG',
                    'Argentina': '&cr=countryAR',
                    'Armenia': '&cr=countryAM',
                    'Aruba': '&cr=countryAW',
                    'Australia': '&cr=countryAU',
                    'Austria': '&cr=countryAT',
                    'Azerbaijan': '&cr=countryAZ',
                    'Bahamas': '&cr=countryBS',
                    'Bahrain': '&cr=countryBH',
                    'Bangladesh': '&cr=countryBD',
                    'Barbados': '&cr=countryBB',
                    'Belarus': '&cr=countryBY',
                    'Belgium': '&cr=countryBE',
                    'Belize': '&cr=countryBZ',
                    'Benin': '&cr=countryBJ',
                    'Bermuda': '&cr=countryBM',
                    'Bhutan': '&cr=countryBT',
                    'Bolivia': '&cr=countryBO',
                    'Bosnia and Herzegovina': '&cr=countryBA',
                    'Botswana': '&cr=countryBW',
                    'Bouvet Island': '&cr=countryBV',
                    'Brazil': '&cr=countryBR',
                    'British Indian Ocean Territory': '&cr=countryIO',
                    'Brunei Darussalam': '&cr=countryBN',
                    'Bulgaria': '&cr=countryBG',
                    'Burkina Faso': '&cr=countryBF',
                    'Burundi': '&cr=countryBI',
                    'Cambodia': '&cr=countryKH',
                    'Cameroon': '&cr=countryCM',
                    'Canada': '&cr=countryCA',
                    'Cape Verde': '&cr=countryCV',
                    'Cayman Islands': '&cr=countryKY',
                    'Central African Republic': '&cr=countryCF',
                    'Chad': '&cr=countryTD',
                    'Chile': '&cr=countryCL',
                    'China': '&cr=countryCN',
                    'Christmas Island': '&cr=countryCX',
                    'Cocos (Keeling) Islands': '&cr=countryCC',
                    'Colombia': '&cr=countryCO',
                    'Comoros': '&cr=countryKM',
                    'Congo': '&cr=countryCD',
                    'Cook Islands': '&cr=countryCK',
                    'Costa Rica': '&cr=countryCR',
                    "Cote d'Ivoire": '&cr=countryCI',
                    'Croatia': '&cr=countryHR',
                    'Cyprus': '&cr=countryCY',
                    'Czech Republic': '&cr=countryCZ',
                    'Denmark': '&cr=countryDK',
                    'Djibouti': '&cr=countryDJ',
                    'Dominica': '&cr=countryDM',
                    'Dominican Republic': '&cr=countryDO',
                    'East Timor': '&cr=countryTL',
                    'Ecuador': '&cr=countryEC',
                    'Egypt': '&cr=countryEG',
                    'El Salvador': '&cr=countrySV',
                    'Equatorial Guinea': '&cr=countryGQ',
                    'Eritrea': '&cr=countryER',
                    'Estonia': '&cr=countryEE',
                    'Ethiopia': '&cr=countryET',
                    'Falkland Islands (Malvinas)': '&cr=countryFK',
                    'Faroe Islands': '&cr=countryFO',
                    'Fiji': '&cr=countryFJ',
                    'Finland': '&cr=countryFI',
                    'France': '&cr=countryFR',
                    'French Guiana': '&cr=countryGF',
                    'French Polynesia': '&cr=countryPF',
                    'French Southern Territories': '&cr=countryTF',
                    'Gabon': '&cr=countryGA',
                    'Gambia': '&cr=countryGM',
                    'Georgia': '&cr=countryGE',
                    'Germany': '&cr=countryDE',
                    'Ghana': '&cr=countryGH',
                    'Gibraltar': '&cr=countryGI',
                    'Greece': '&cr=countryGR',
                    'Greenland': '&cr=countryGL',
                    'Grenada': '&cr=countryGD',
                    'Guadeloupe': '&cr=countryGP',
                    'Guam': '&cr=countryGU',
                    'Guatemala': '&cr=countryGT',
                    'Guinea': '&cr=countryGN',
                    'Guinea-Bissau': '&cr=countryGW',
                    'Guyana': '&cr=countryGY',
                    'Haiti': '&cr=countryHT',
                    'Heard and McDonald Islands': '&cr=countryHM',
                    'Honduras': '&cr=countryHN',
                    'Hong Kong': '&cr=countryHK',
                    'Hungary': '&cr=countryHU',
                    'Iceland': '&cr=countryIS',
                    'India': '&cr=countryIN',
                    'Indonesia': '&cr=countryID',
                    'Iraq': '&cr=countryIQ',
                    'Ireland': '&cr=countryIE',
                    'Israel': '&cr=countryIL',
                    'Italy': '&cr=countryIT',
                    'Jamaica': '&cr=countryJM',
                    'Japan': '&cr=countryJP',
                    'Jordan': '&cr=countryJO',
                    'Kazakhstan': '&cr=countryKZ',
                    'Kenya': '&cr=countryKE',
                    'Kiribati': '&cr=countryKI',
                    'Kuwait': '&cr=countryKW',
                    'Kyrgyzstan': '&cr=countryKG',
                    "Lao People's Democratic Republic": '&cr=countryLA',
                    'Latvia': '&cr=countryLV',
                    'Lebanon': '&cr=countryLB',
                    'Lesotho': '&cr=countryLS',
                    'Liberia': '&cr=countryLR',
                    'Libya': '&cr=countryLY',
                    'Liechtenstein': '&cr=countryLI',
                    'Lithuania': '&cr=countryLT',
                    'Luxembourg': '&cr=countryLU',
                    'Macau': '&cr=countryMO',
                    'Macedonia': '&cr=countryMK',
                    'Madagascar': '&cr=countryMG',
                    'Malawi': '&cr=countryMW',
                    'Malaysia': '&cr=countryMY',
                    'Maldives': '&cr=countryMV',
                    'Mali': '&cr=countryML',
                    'Malta': '&cr=countryMT',
                    'Marshall Islands': '&cr=countryMH',
                    'Martinique': '&cr=countryMQ',
                    'Mauritania': '&cr=countryMR',
                    'Mauritius': '&cr=countryMU',
                    'Mayotte': '&cr=countryYT',
                    'Mexico': '&cr=countryMX',
                    'Micronesia': '&cr=countryFM',
                    'Moldova': '&cr=countryMD',
                    'Monaco': '&cr=countryMC',
                    'Mongolia': '&cr=countryMN',
                    'Montserrat': '&cr=countryMS',
                    'Morocco': '&cr=countryMA',
                    'Mozambique': '&cr=countryMZ',
                    'Namibia': '&cr=countryNA',
                    'Nauru': '&cr=countryNR',
                    'Nepal': '&cr=countryNP',
                    'Netherlands': '&cr=countryNL',
                    'Netherlands Antilles': '&cr=countryAN',
                    'New Caledonia': '&cr=countryNC',
                    'New Zealand': '&cr=countryNZ',
                    'Nicaragua': '&cr=countryNI',
                    'Niger': '&cr=countryNE',
                    'Nigeria': '&cr=countryNG',
                    'Niue': '&cr=countryNU',
                    'Norfolk Island': '&cr=countryNF',
                    'Northern Maria': '&cr=countryMP',
                    'Norway': '&cr=countryNO',
                    'Oman': '&cr=countryOM',
                    'Pakistan': '&cr=countryPK',
                    'Palau': '&cr=countryPW',
                    'Palestinian Territory': '&cr=countryPS',
                    'Panama': '&cr=countryPA',
                    'Papua New Guinea': '&cr=countryPG',
                    'Paraguay': '&cr=countryPY',
                    'Peru': '&cr=countryPE',
                    'Philippines': '&cr=countryPH',
                    'Pitcairn': '&cr=countryPN',
                    'Poland': '&cr=countryPL',
                    'Portugal': '&cr=countryPT',
                    'Puerto Rico': '&cr=countryPR',
                    'Qatar': '&cr=countryQA',
                    'Reunion': '&cr=countryRE',
                    'Romania': '&cr=countryRO',
                    'Russian Federation': '&cr=countryRU',
                    'Rwanda': '&cr=countryRW',
                    'Saint Kitts and Nevis': '&cr=countryKN',
                    'Saint Lucia': '&cr=countryLC',
                    'Saint Vincent and the Grenadines': '&cr=countryVC',
                    'Samoa': '&cr=countryWS',
                    'San Marino': '&cr=countrySM',
                    'Sao Tome and Principe': '&cr=countryST',
                    'Saudi Arabia': '&cr=countrySA',
                    'Senegal': '&cr=countrySN',
                    'Serbia and Montenegro': '&cr=countryCS',
                    'Seychelles': '&cr=countrySC',
                    'Sierra Leone': '&cr=countrySL',
                    'Singapore': '&cr=countrySG',
                    'Slovakia': '&cr=countrySK',
                    'Slovenia': '&cr=countrySI',
                    'Solomon Islands': '&cr=countrySB',
                    'Somalia': '&cr=countrySO',
                    'South Africa': '&cr=countryZA',
                    'South Georgia and The South Sandwich Islands': '&cr=countryGS',
                    'South Korea': '&cr=countryKR',
                    'Spain': '&cr=countryES',
                    'Sri Lanka': '&cr=countryLK',
                    'St. Helena': '&cr=countrySH',
                    'St. Pierre and Miquelon': '&cr=countryPM',
                    'Suriname': '&cr=countrySR',
                    'Svalbard and Jan Mayen Islands': '&cr=countrySJ',
                    'Swaziland': '&cr=countrySZ',
                    'Sweden': '&cr=countrySE',
                    'Switzerland': '&cr=countryCH',
                    'Taiwan': '&cr=countryTW',
                    'Tajikistan': '&cr=countryTJ',
                    'Tanzania': '&cr=countryTZ',
                    'Thailand': '&cr=countryTH',
                    'Togo': '&cr=countryTG',
                    'Tokelau': '&cr=countryTK',
                    'Tonga': '&cr=countryTO',
                    'Trinidad and Tobago': '&cr=countryTT',
                    'Tunisia': '&cr=countryTN',
                    'Turkey': '&cr=countryTR',
                    'Turkmenistan': '&cr=countryTM',
                    'Turks and Caicos Islands': '&cr=countryTC',
                    'Tuvalu': '&cr=countryTV',
                    'Uganda': '&cr=countryUG',
                    'Ukraine': '&cr=countryUA',
                    'United Arab Emirates': '&cr=countryAE',
                    'United Kingdom': '&cr=countryGB',
                    'United States': '&cr=countryUS',
                    'United States Minor Outlying Islands': '&cr=countryUM',
                    'Uruguay': '&cr=countryUY',
                    'Uzbekistan': '&cr=countryUZ',
                    'Vanuatu': '&cr=countryVU',
                    'Vatican': '&cr=countryVA',
                    'Venezuela': '&cr=countryVE',
                    'Viet Nam': '&cr=countryVN',
                    'Virgin Islands (British)': '&cr=countryVG',
                    'Virgin Islands (U.S.)': '&cr=countryVI',
                    'Wallis and Futuna Islands': '&cr=countryWF',
                    'Western Sahara': '&cr=countryEH',
                    'Yemen': '&cr=countryYE',
                    'Zambia': '&cr=countryZM',
                    'Zimbabwe': '&cr=countryZW'}
        
        return countries_dict
    ##########################################################################################################################################################################################################
    

    
    ########################################################################################################################################################################################################## 
    def term_apperaing():
        term_dict = {
                'Anywhere': '&as_occt=any',
                'In Title': '&as_occt=title',
                'In Text': '&as_occt=body',
                'In URL': '&as_occt=url',
                'In Links': '&as_occt=links'}
        
        return term_dict
    ##########################################################################################################################################################################################################    
    
    
    ########################################################################################################################################################################################################## 
    def file_type():
        types_dict= {'File Type': '',
                    'PDF': '&as_filetype=pdf',
                    'Adobe Postscript': '&as_filetype=ps',
                    'Autodesk': '&as_filetype=dwf',
                    'Google Earth KML': '&as_filetype=kml',
                    'Google Earth KMZ': '&as_filetype=kmz',
                    'Microsoft Excel': '&as_filetype=xls',
                    'Microsoft powerpoint': '&as_filetype=ppt',
                    'Microsoft Word': '&as_filetype=doc',
                    'Rich Text Format': '&as_filetype=rtf',
                    'Shockwave flash': '&as_filetype=swf'}
        
        return types_dict
    ##########################################################################################################################################################################################################