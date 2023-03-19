from faker import Faker
fake = Faker()

class movies:
    def __init__(self, title, year, genre, play_counts):
        self.title = title
        self.year = year
        self.genre = genre
        self.play_counts = play_counts

    def __str__(self):
      return f"{self.title} {self.year} {self.genre} {self.play_counts}"
    
    def play(self):
      self.play_counts = self.play_counts + 1
      self.title
      return f"{self.title} {self.year}, Liczba wyświetleń: {self.play_counts}"
    
    
      
    

class series(movies):
    def __init__(self, num_episode, num_season, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.num_episode = num_episode
         self.num_season = num_season    
    
    def __str__(self):
         return f"{self.title} {self.year} {self.genre} {self.num_episode} {self.num_season} {self.play_counts}"
    
    season = ""
    def play(self):
        self.play_counts = self.play_counts + 1
        self.title = self.title
        season = str(self.num_season)
        if len(season) == 1:
            season = "0"
            self.num_season = str(self.num_season)
            self.num_season = season + self.num_season
            if len(str(self.num_episode)) <= 1:
                self.num_episode = str(self.num_episode)
                self.num_episode = "0" + self.num_episode
        else:
            self.num_season = "1"
            self.num_season = str(self.num_season)
            self.num_season = self.num_season + self.num_season
            if len(str(self.num_episode)) <= 1:
                self.num_episode = str(self.num_episode)
                self.num_episode = "0" + self.num_episode
        return f"{self.title} S{self.num_season} E{self.num_episode} Liczba wyświetleń: {self.play_counts}."
    
    

        
#tworzę kino, dodaję filmy i seriale:
if __name__ == '__main__':
 
    cinema = [
        movies("Pulp Fiction", "1994", "adventure", 0),
        movies("The Shawshank Redemption", "1994", "drama", 0),
        movies("Fight Club", "1999", "thriller", 0),
        movies("Intouchables", "2011", "drama", 0),
        movies("The Godfather", "1972", "drama", 0),
        series(title="House M.D.", year="2004 - 2012", genre="drama", num_episode= 15, num_season= 1, play_counts=0),
        series(title="Breaking Bad", year="2008 - 2013", genre="drama", num_episode= 1, num_season= 2, play_counts=0),
        series(title="Friends", year="1994 - 2004", genre="comedy", num_episode= 1, num_season= 1, play_counts=0),
        series(title="Vikings", year="2013 - 2020", genre="drama", num_episode= 1, num_season= 3, play_counts=0),
        series(title="Wataha", year="2019 - 2020", genre="thriller", num_episode= 1, num_season= 3, play_counts=0)    
    ]

#sortuję kino
cinema.sort(key=lambda x: x.title, reverse=False)

#drukuję kino
for i in cinema:
    print(i)
print()

#oglądam pierwszy raz
play_m = cinema[0].play()
print(play_m)

#oglądam drugi raz
play_m = cinema[0].play()
print(play_m)

#oglądam serial
play_s = cinema[9].play()
print(play_s)

#i powtórkę
play_s = cinema[9].play()
print(play_s)
print()


def get_series(cinema):
    list_of_series = []
    for issue in cinema:
      if isinstance(issue, series) == True:
         list_of_series.append(str(issue))    
    return list_of_series
getseries = get_series(cinema)
print(getseries)
print()

def get_series(cinema):
    list_of_movies = []
    for issue in cinema:
      if isinstance(issue, series) == False:
         list_of_movies.append(str(issue))    
    return list_of_movies
getseries = get_series(cinema)
print(getseries)
print()

def search(list, title):
    x = 0
    for issue in list:
        x = x+1
        if issue.title != title:
            if x == len(list):
                print("Nie ma takiej pozycji w kinie")
        if issue.title == title:
            print(title)
            break
if __name__ == "__main__":
    item_text = input("Podaj nazwę filmu bądź serialu: ")
    searching_result = search(cinema,item_text)
    #print(searching_result)

def generate_views(list, title):
    for issue in list:
        if issue.title:
            issue.play_counts = fake.random_int(0, 100)
    return issue.play_counts
gen_view = generate_views(cinema, cinema[0])
print(gen_view)
print()

def generate_views_10_times(list, title):
    the_list = []
    for issue in list:
        if issue.title:
            issue.play_counts = fake.random_int(0, 100)
            the_list.append(issue.play_counts)
    return the_list
gen_view_10 = generate_views_10_times(cinema,cinema[0])
print(gen_view_10)

def top_tiles(list,number):
    the_list= []
    for issue in list:
        list.sort(key=lambda x: x.play_counts, reverse=True)
        del list[number:len(list)]
    return list
tp_titles = top_tiles(cinema,3)

for issue in tp_titles:
    print(issue.title)