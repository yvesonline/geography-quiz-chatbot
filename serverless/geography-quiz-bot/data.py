#!/usr/bin/env python3
# encoding: utf-8

COUNTRY_TO_CAPITAL = {
    "Abkhazia": "Sukhumi",
    "Afghanistan": "Kabul",
    "Akrotiri and Dhekelia": "Episkopi Cantonment",
    "Albania": "Tirana",
    "Algeria": "Algiers",
    "American Samoa": "Pago Pago",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
    "Anguilla": "The Valley",
    "Antigua and Barbuda": "St. John's",
    "Argentina": "Buenos Aires",
    "Armenia": "Yerevan",
    "Aruba": "Oranjestad",
    "Ascension Island": "Georgetown",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Bahamas": "Nassau",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Barbados": "Bridgetown",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Belize": "Belmopan",
    "Benin": "Porto-Novo",
    "Bermuda": "Hamilton",
    "Bhutan": "Thimphu",
    "Bolivia": "La Paz",
    "Bosnia and Herzegovina": "Sarajevo",
    "Botswana": "Gaborone",
    "Brazil": "Bras\u00edlia",
    "British Virgin Islands": "Road Town",
    "Brunei": "Bandar Seri Begawan",
    "Bulgaria": "Sofia",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Bujumbura",
    "Cambodia": "Phnom Penh",
    "Cameroon": "Yaound\u00e9",
    "Canada": "Ottawa",
    "Cape Verde": "Praia",
    "Cayman Islands": "George Town",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Chile": "Santiago",
    "China": "Beijing",
    "Christmas Island": "Flying Fish Cove",
    "Cocos (Keeling) Islands": "West Island",
    "Colombia": "Bogot\u00e1",
    "Comoros": "Moroni",
    "Cook Islands": "Avarua",
    "Costa Rica": "San Jos\u00e9",
    "Croatia": "Zagreb",
    "Cuba": "Havana",
    "Cura\u00e7ao": "Willemstad",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "C\u00f4te d'Ivoire": "Yamoussoukro",
    "Democratic Republic of the Congo": "Kinshasa",
    "Denmark": "Copenhagen",
    "Djibouti": "Djibouti",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "East Timor (Timor-Leste)": "Dili",
    "Easter Island": "Hanga Roa",
    "Ecuador": "Quito",
    "Egypt": "Cairo",
    "El Salvador": "San Salvador",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Estonia": "Tallinn",
    "Ethiopia": "Addis Ababa",
    "Falkland Islands": "Stanley",
    "Faroe Islands": "T\u00f3rshavn",
    "Federated States of Micronesia": "Palikir",
    "Fiji": "Suva",
    "Finland": "Helsinki",
    "France": "Paris",
    "French Guiana": "Cayenne",
    "French Polynesia": "Papeete",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Ghana": "Accra",
    "Gibraltar": "Gibraltar",
    "Greece": "Athens",
    "Greenland": "Nuuk",
    "Grenada": "St. George's",
    "Guam": "Hag\u00e5t\u00f1a",
    "Guatemala": "Guatemala City",
    "Guernsey": "St. Peter Port",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Guyana": "Georgetown",
    "Haiti": "Port-au-Prince",
    "Honduras": "Tegucigalpa",
    "Hungary": "Budapest",
    "Iceland": "Reykjav\u00edk",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Ireland": "Dublin",
    "Isle of Man": "Douglas",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Jamaica": "Kingston",
    "Japan": "Tokyo",
    "Jersey": "St. Helier",
    "Jordan": "Amman",
    "Kazakhstan": "Astana",
    "Kenya": "Nairobi",
    "Kiribati": "Tarawa",
    "Kosovo": "Pristina",
    "Kuwait": "Kuwait City",
    "Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane",
    "Latvia": "Riga",
    "Lebanon": "Beirut",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Macedonia": "Skopje",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Malaysia": "Kuala Lumpur",
    "Maldives": "Mal\u00e9",
    "Mali": "Bamako",
    "Malta": "Valletta",
    "Marshall Islands": "Majuro",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Mexico": "Mexico City",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Mongolia": "Ulaanbaatar",
    "Montenegro": "Podgorica",
    "Montserrat": "Plymouth",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Myanmar": "Naypyidaw",
    "Nagorno-Karabakh Republic": "Stepanakert",
    "Namibia": "Windhoek",
    "Nauru": "Yaren",
    "Nepal": "Kathmandu",
    "Netherlands": "Amsterdam",
    "New Caledonia": "Noum\u00e9a",
    "New Zealand": "Wellington",
    "Nicaragua": "Managua",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "Niue": "Alofi",
    "Norfolk Island": "Kingston",
    "North Korea": "Pyongyang",
    "Northern Cyprus": "Nicosia",
    "United Kingdom Northern Ireland": "Belfast",
    "Northern Mariana Islands": "Saipan",
    "Norway": "Oslo",
    "Oman": "Muscat",
    "Pakistan": "Islamabad",
    "Palau": "Ngerulmud",
    "Palestine": "Jerusalem",
    "Panama": "Panama City",
    "Papua New Guinea": "Port Moresby",
    "Paraguay": "Asunci\u00f3n",
    "Peru": "Lima",
    "Philippines": "Manila",
    "Pitcairn Islands": "Adamstown",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Puerto Rico": "San Juan",
    "Qatar": "Doha",
    "Republic of China (Taiwan)": "Taipei",
    "Republic of the Congo": "Brazzaville",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "Rwanda": "Kigali",
    "Saint Barth\u00e9lemy": "Gustavia",
    "Saint Helena": "Jamestown",
    "Saint Kitts and Nevis": "Basseterre",
    "Saint Lucia": "Castries",
    "Saint Martin": "Marigot",
    "Saint Pierre and Miquelon": "St. Pierre",
    "Saint Vincent and the Grenadines": "Kingstown",
    "Samoa": "Apia",
    "San Marino": "San Marino",
    "Saudi Arabia": "Riyadh",
    "Scotland": "Edinburgh",
    "Senegal": "Dakar",
    "Serbia": "Belgrade",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Singapore": "Singapore",
    "Sint Maarten": "Philipsburg",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Solomon Islands": "Honiara",
    "Somalia": "Mogadishu",
    "Somaliland": "Hargeisa",
    "South Africa": "Pretoria",
    "South Georgia and the South Sandwich Islands": "Grytviken",
    "South Korea": "Seoul",
    "South Ossetia": "Tskhinvali",
    "South Sudan": "Juba",
    "Spain": "Madrid",
    "Sri Lanka": "Sri Jayawardenapura Kotte",
    "Sudan": "Khartoum",
    "Suriname": "Paramaribo",
    "Swaziland": "Mbabane",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Syria": "Damascus",
    "S\u00e3o Tom\u00e9 and Pr\u00edncipe": "S\u00e3o Tom\u00e9",
    "Tajikistan": "Dushanbe",
    "Tanzania": "Dodoma",
    "Thailand": "Bangkok",
    "Togo": "Lom\u00e9",
    "Tonga": "Nuku\u02bbalofa",
    "Transnistria": "Tiraspol",
    "Trinidad and Tobago": "Port of Spain",
    "Tristan da Cunha": "Edinburgh of the Seven Seas",
    "Tunisia": "Tunis",
    "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat",
    "Turks and Caicos Islands": "Cockburn Town",
    "Tuvalu": "Funafuti",
    "Uganda": "Kampala",
    "Ukraine": "Kiev",
    "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "United States Virgin Islands": "Charlotte Amalie",
    "Uruguay": "Montevideo",
    "Uzbekistan": "Tashkent",
    "Vanuatu": "Port Vila",
    "Vatican City": "Vatican City",
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Wales": "Cardiff",
    "Wallis and Futuna": "Mata-Utu",
    "Western Sahara": "El Aai\u00fan",
    "Yemen": "Sana\u00e1",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}
