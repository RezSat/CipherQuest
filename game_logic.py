import random
from ciphers import caesar_cipher

common_phrases = ['A piece of cake', 'Jump on the bandwagon', 'Bite the bullet', "Don't count your chickens before they hatch", "Don't put all your eggs in one basket", 'Actions speak louder than words', 'Cutting corners', 'Cry over spilled milk', 'Under the weather', 'The ball is in your court', 'Take with a grain of salt', 'Hit the nail on the head', 'All in the same boat', 'Hit the hay', 'Throw in the towel', 'Piece of cake', 'Cut to the chase', 'Let the cat out of the bag', 'Burn the midnight oil', 'Break a leg', 'Cost an arm and a leg', 'Spill the beans', 'Break the ice', "Don't cry over spilled milk", 'Every cloud has a silver lining', 'Kick the bucket']
country_names = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
    "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica",
    "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
    "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland",
    "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica",
    "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo",
    "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
    "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru",
    "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea"
]

capitals = [
    "Kabul", "Tirana", "Algiers", "Andorra la Vella", "Luanda", "St. John's", "Buenos Aires", "Yerevan",
    "Canberra", "Vienna", "Baku", "Nassau", "Manama", "Dhaka", "Bridgetown", "Minsk", "Brussels", "Belmopan",
    "Porto-Novo", "Thimphu", "Sucre", "Sarajevo", "Gaborone", "Brasília", "Bandar Seri Begawan", "Sofia",
    "Ouagadougou", "Bujumbura", "Praia", "Phnom Penh", "Yaoundé", "Ottawa", "Bangui", "N'Djamena", "Santiago",
    "Beijing", "Bogotá", "Moroni", "Brazzaville", "San José", "Zagreb", "Havana", "Nicosia", "Prague",
    "Copenhagen", "Djibouti", "Roseau", "Santo Domingo", "Dili", "Quito", "Cairo", "San Salvador", "Malabo",
    "Asmara", "Tallinn", "Mbabane","Lobamba", "Addis Ababa", "Suva",
    "Helsinki", "Paris", "Libreville", "Banjul", "Tbilisi", "Berlin", "Accra", "Athens", "St. George's",
    "Guatemala", "Conakry", "Bissau", "Georgetown", "Port-au-Prince", "Tegucigalpa", "Budapest", "Reykjavik",
    "New Delhi", "Jakarta", "Tehran", "Baghdad", "Dublin", "Jerusalem", "Rome", "Yamoussoukro", "Kingston",
    "Tokyo", "Amman", "Nur-Sultan", "Nairobi", "Tarawa", "Pyongyang", "Seoul", "Pristina", "Kuwait",
    "Bishkek", "Vientiane", "Riga", "Beirut", "Maseru", "Monrovia", "Tripoli", "Vaduz", "Vilnius", "Luxembourg",
    "Antananarivo", "Lilongwe", "Kuala Lumpur", "Malé", "Bamako", "Valletta", "Majuro", "Nouakchott", "Port Louis",
    "Mexico", "Palikir", "Chisinau", "Monaco", "Ulaanbaatar", "Podgorica", "Rabat", "Maputo", "Naypyidaw",
    "Windhoek", "Yaren", "Kathmandu", "Amsterdam", "Wellington", "Managua", "Niamey", "Abuja", "Skopje",
    "Oslo", "Muscat", "Islamabad", "Ngerulmud", "Ramallah", "Panama"
]

physics_nobel_winners = ['Leon Cooper', 'John Bardeen', 'Masatoshi Koshiba', 'Arthur Ashkin', 'Kai Siegbahn', 'Sir Harold W. Kroto', 'Albert L. A. Michelson', 'Duncan Haldane', 'Peter Grünberg', 'William D. Phillips', 'Vitaly Ginzburg', 'Carl E. Wieman', 'Robert Schrieffer', 'Steven Chu', 'Horst L. Störmer', 'Robert F. Curl Jr.', 'Richard Feynman', 'John L. Hall', 'Isamu Akasaki', 'Kazuo Kuroda', 'Shinya Yamanaka', 'Robert Laughlin', 'Zhores Alferov', 'Enrico Fermi', 'Harvey J. Alter', 'Horst Ludwig Störmer', 'Alexei Abrikosov', 'David J. Thouless', 'John C. Mather', 'Arthur A. Schawlow', 'Riccardo Giacconi', 'Paul Dirac', 'Niels Bohr', 'Patrick Schön', 'Takaaki Kajita', 'Wilhelm Conrad Roentgen', 'Wolfgang Ketterle', 'Arthur L. Schawlow', 'Theodor W. Hänsch', 'Albert Einstein', 'Toshihide Maskawa', 'Hendrik Lorentz', 'Steven Weinberg', 'George F. Smoot', 'Alain Aspect', 'Yoichiro Nambu', 'Subrahmanyan Chandrasekhar', 'Gérard Mourou', 'Donna Strickland', 'Nicolaas Bloembergen', 'Horst Störmer', 'John M. Kosterlitz', 'Claude Cohen-Tannoudji', 'Max Planck', 'Serge Haroche', 'Daniel C. Tsui', 'Julian Schwinger', 'Michael Houghton', 'Charles M. Rice', 'Richard E. Smalley', 'Makoto Kobayashi', 'Hiroshi Amano', 'Daniel Tsui', 'Robert H. Grubbs', 'Koshiba Masatoshi', 'Ahmed Zewail', 'Yves Chauvin', 'Willis E. Lamb', 'Werner Heisenberg', 'Robert B. Laughlin', 'Albert Fert', 'Arthur Leonard Schawlow', 'Shinichiro Tomonaga', 'Yoshinori Ohsumi', 'Eric A. Cornell', 'Raymond Davis Jr.', 'Pieter Zeeman', 'Marie Curie', 'Kai M. Siegbahn', 'Polykarp Kusch', 'Erwin Schrödinger', 'Laureate in Physics', 'F. Duncan M. Haldane', 'David J. Wineland']


collection = {
    "PHYSICS NOBEL PRIZE WINNERS" : {"list":physics_nobel_winners, "desc": "This is a physics Nobel prize winner"}, 
    "COUNTRY NAMES" : {"list":country_names, "desc": "This is a country"},
    "CAPITALS": {"list":capitals, "desc": "This is a capital"}
}
class GameLogic:
    def __init__(self) -> None:
        self.current_level = 1
        self.max_level = 5 #for now
        self.score = 0
        self.hint_used = False

    def generate_random_message(self):
        rlist = random.choice(list(collection.keys()))
        rm = random.choice(collection[rlist]['list'])

        return rm.lower(), collection[rlist]['desc']

    def encrypt_message(self, message, cipher_type="caesar"):
        return caesar_cipher(message, random.randrange(1,20))

    def check_solution(self, player_solution, original):
        if player_solution == original:
            return True
        else:
            return False

    def update_score(self, time_taken=None):
        score = 10
        if self.hint_used:
            score = 5
        self.score += score
        

    def next_level(self):
        pass