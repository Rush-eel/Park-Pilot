import streamlit as st
from google.cloud import firestore
from PIL import Image
from streamlit_folium import folium_static
import folium

db = firestore.Client.from_service_account_json("firestore-key.json")

doc_ref = db.collection("attractions")
doc_ref_preserves = db.collection("preserves")
doc_ref_reserves = db.collection("reserves")
doc_ref_rivers = db.collection("rivers")
doc_ref_seashores = db.collection("seashores")
image = Image.open('assets/0.jpeg')
st.set_page_config(page_title="Website",
                   layout="wide",
                   )
tab1, tab2, tab4 = st.tabs(["Dashboard ⛰", "Map📍", "Opportunities ❤️"])

with tab1:
    st.title('A faster way to search for your next nature destination')
    st.subheader("Welcome to Park Pilot!")
    st.write('Explore natures treasures effortlessly – find national forests, parks, seashores, and beyond ')

    st.divider()
    st.write('Park Pilot is your directory to your next natural wonder. Park Pilot is dedicated to help motivate people get out into the great outdoors, and find a love for nature, and protecting it.')

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/3.jpeg")
        st.caption('Big Bend National Park')

    with col2:
        st.image("assets/15.jpeg")
        st.caption('Dry Tortugas National Park')



    ParksTab, PreservesTab, SeashoresTab, RiversTab, ReservesTab = st.tabs(["National Parks",
                                                                  "National Preserves",
                                                                  "National Seashores",
                                                                  "National Rivers",
                                                                  "National Reserves"])
    with ParksTab:
        st.write("A national park is a protected area of natural beauty and ecological significance, preserved for public enjoyment and conservation.")
        for doc in doc_ref.stream():
                st.subheader(doc.get("name"))
                st.caption(doc.get("description",))
                st.divider()
                coll, colk = st.columns(2)

                with colk:
                    st.subheader("More information on" + " " + doc.get("name") + ":")
                    st.write("State:")
                    st.caption(doc.get("state"))
                    st.write("")
                    st.write("Website:")
                    st.caption(doc.get("website"))
                    st.write("")
                    st.write("Coordinates (latitude, longitude):")
                    st.caption(doc.get('latitude'))
                    st.caption(doc.get('longitude'))
                with coll:
                    st.image("assets/" + str(doc.get("id")) + ".jpeg")
                st.divider()


    with PreservesTab:
        for doc in doc_ref_preserves.stream():
                st.subheader(doc.get("name"))
                st.caption(doc.get("description",))
                st.divider()
                firstcol, secondcol = st.columns(2)
                with secondcol:
                    st.subheader("More information on" + " " + doc.get("name") + ":")
                    st.write("State:")
                    st.caption(doc.get("state"))
                    st.write("")
                    st.write("Website:")
                    st.caption(doc.get("website"))
                    st.write("")
                    st.write("Coordinates (latitude, longitude):")
                    st.caption(doc.get('latitude'))
                    st.caption(doc.get('longitude'))
                with firstcol:
                    st.image("assets/" + str(doc.get("id")) + "preserves" + ".jpeg")
                st.divider()

    with RiversTab:
        for doc in doc_ref_rivers.stream():
                st.subheader(doc.get("name"))
                st.caption(doc.get("description",))
                st.divider()
                firstcoll, secondcoll = st.columns(2)
                with secondcoll:
                    st.subheader("More information on" + " " + doc.get("name") + ":")
                    st.write("State:")
                    st.caption(doc.get("state"))
                    st.write("")
                    st.write("Website:")
                    st.caption(doc.get("website"))
                    st.write("")
                    st.write("Coordinates (latitude, longitude):")
                    st.caption(doc.get('latitude'))
                    st.caption(doc.get('longitude'))
                with firstcoll:
                    st.image("assets/" + str(doc.get("id")) + "rivers" + ".jpeg")
                st.divider()

    with ReservesTab:
        for doc in doc_ref_reserves.stream():
                st.subheader(doc.get("name"))
                st.caption(doc.get("description",))
                st.divider()
                firstcolll, secondcolll = st.columns(2)
                with secondcolll:
                    st.subheader("More information on" + " " + doc.get("name") + ":")
                    st.write("State:")
                    st.caption(doc.get("state"))
                    st.write("")
                    st.write("Website:")
                    st.caption(doc.get("website"))
                    st.write("")
                    st.write("Coordinates (latitude, longitude):")
                    st.caption(doc.get('latitude'))
                    st.caption(doc.get('longitude'))
                with firstcolll:
                    st.image("assets/" + str(doc.get("id")) + "reserves" + ".jpeg")
                st.divider()

    with SeashoresTab:
        for doc in doc_ref_seashores.stream():
                st.subheader(doc.get("name"))
                st.caption(doc.get("description",))
                st.divider()
                firstcollll, secondcollll = st.columns(2)
                with secondcollll:
                    st.subheader("More information on" + " " + doc.get("name") + ":")
                    st.write("State:")
                    st.caption(doc.get("state"))
                    st.write("")
                    st.write("Website:")
                    st.caption(doc.get("website"))
                    st.write("")
                    st.write("Coordinates (latitude, longitude):")
                    st.caption(doc.get('latitude'))
                    st.caption(doc.get('longitude'))
                with firstcollll:
                    st.image("assets/" + str(doc.get("id")) + "seashores" + ".jpeg")
                st.divider()

with tab2:
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=1)
    for doc in doc_ref.stream():
        folium.Marker(
            [doc.get("latitude"), doc.get("longitude")], popup=doc.get("name")
        ).add_to(m)

    folium_static(m)




with tab4:
    emptycol, fullcol, emtcol = st.columns(3)
    with emptycol:
        st.write(' ')
    with fullcol:
        st.title("YOU CAN HELP MAKE A DIFFERENCE!")
    with emtcol:
        st.write(' ')

    st.header("Preservation areas hold significant importance in protecting the Earth's natural resources "
    "and diverse ecosystems. They serve as vital habitats for numerous plant and animal species, "
    "ensuring ecological stability and the sustainability of natural systems. These regions also "
    "contribute to the regulation of climate, water sources, and air purity, thus supporting overall "
    "environmental well-being. Moreover, preservation areas provide essential opportunities for "
    "scientific study, learning, and leisure activities, fostering a deeper comprehension of the "
    "natural world and encouraging environmental responsibility among people. By conserving "
    "these areas, we can ensure the protection of our natural legacy for future generations and"
    "maintain the overall health of the planet.")
    st.divider()
    st.subheader("Definition of Preservation and Conservation:")
    st.caption("https://education.nationalgeographic.org/resource/preservation/")
    st.divider()
    st.subheader("Donate:")
    st.write("National Parks Conservation Association:")
    st.caption("https://support.npca.org/page/41642/donate/1?ea.tracking.id=io5dl27h")
    st.write("The National Parks Foundation:")
    st.caption("http://give.nationalparks.org/site/Donation2?df_id=1520&1520.donation=form1&mfc_pref=T")
    st.write("National Park Service:")
    st.caption("https://www.nps.gov/subjects/partnerships/donate.htm")
    st.divider()
    st.subheader("Volunteer:")
    st.caption("Volunteer.gov: https://www.volunteer.gov/s/global-search/FILTERNPS")
    st.caption("Become a Volunteer: https://www.nps.gov/subjects/volunteer/become.htm")
    st.caption("Resources for Volunteers: https://www.nps.gov/subjects/volunteer/resources.htm")
    st.divider()
    st.subheader("More ways to help:")
    st.write(" - Advocate for sustainable policies")
    st.write(" - Joining public forums to raise awareness")
    st.write(" - Provide knowledge on responsible tourism")
    st.write(" - Support local businesses")
    st.write(" - Engage in citizen science projects")

    st.write(
        "You cannot get through a single day without having an impact on the world around you. What you do makes a difference, and you have to decide what kind of a difference you want it to make --  Jane Goodall")

