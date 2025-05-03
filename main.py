import streamlit as st

class Transport:
    def __init__(self, name, route, fare, timings):
        self.name = name
        self.route = route
        self.fare = fare
        self.timings = timings

    def display_info(self):
        st.subheader(self.name)
        st.write(f"🛣️ Route: {self.route}")
        st.write(f"💸 Fare: Rs. {self.fare}")
        st.write(f"⏰ Timings: {self.timings}")
        st.markdown("---")


transports = [
    Transport("People Bus Route 1", "Khokrapar to Dockyard", 50, "6:00 AM - 10:00 PM"),
    Transport("People Bus Route 2", "Power House to Indus Hospital", 50, "7:00 AM - 8:00 PM"),
    Transport("People Bus Route 3", "Power House to Nasir Jump", 50, "6:30 AM - 9:00 PM"),
    Transport("People Bus Route 4", "Power House to Keemari", 50, "7:00 AM - 8:00 PM"),
    Transport("People Bus Route 8", "Yousuf Goth to Tower", 50, "7:00 AM - 8:00 PM"),
    Transport("People Bus Route 9", "Gulshan e Hadeed to Tower", 50, "7:00 AM - 8:00 PM"),
    Transport("People Bus Route 10", "Numaish Chowrangi to Ibrahim Hyderi", 50, "7:00 AM - 8:00 PM"),
    Transport("People Bus Route 11", "Miran Nakka to Shireen Jinnah Colony", 50, "7:00 AM - 8:00 PM"),
    Transport("People Bus Route 12", "Naddi Kinara to Lucky Star", 50, "7:00 AM - 8:00 PM"),
    Transport("People Bus Route 13", "Hawksbay to Tower", 50, "7:00 AM - 8:00 PM"),
    Transport("Electric Bus EV-1", "Malir Cantt to Dolmen Mall Clifton", 100, "7:00 AM - 8:00 PM"),
    Transport("Electric Bus EV-2", "Bahria Town to Malir Halt", 100, "7:00 AM - 8:00 PM"),
    Transport("Electric Bus EV-3", "Malir Cantt CheckPost 5 to Numaish", 100, "7:00 AM - 8:00 PM"),
    Transport("Electric Bus EV-4", "Bahria Town to Ayesha Manzil", 100, "7:00 AM - 8:00 PM"),
    Transport("Electric Bus EV-5", "DHA City to Sohrab Goth", 100, "7:00 AM - 8:00 PM"),
    Transport("Mini Bus F-11", "Gul Ahmed Textile Mills to Mustafabad Colony", 0 , "7:00 AM - 8:00 PM"),
    Transport("Mini Bus W-11", "New Karachi Allahwala Masjid to Keemari", 0, "7:00 AM - 8:00 PM"),
    Transport("Mini Bus Gulistan Coach", "Pehlwan Goth to Qayyumabad", 0 , "7:00 AM - 8:00 PM"),
    Transport("Mini Bus Data Coach", "KDA Site Office to Abdul Shah Ghazi Mazar", 0, "7:00 AM - 8:00 PM"),
    Transport("Mini Bus Sheraz Coach", "Picadilly to Hawskbay", 0, "7:00 AM - 8:00 PM"),
]


st.title("🚍 Public Transport Finder")

transport_names = [t.name for t in transports]
selected = st.selectbox("Select a transport:", ["Select Transport"] + transport_names)

if selected != "Select Transport":
    for t in transports:
        if selected == t.name:
            t.display_info()
            break



