class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, hall_no, rows, cols) -> None:
        self.__hall_no = hall_no
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__seats = {}
    
    def valid_show_id(self, id):
        for movie in self.__show_list:
            if movie[0] == id:
                return True
        return False

    def entry_show(self, id, movie_name, time):
        movie = (id, movie_name, time)
        self.__show_list.append(movie)
        main = []
        tmp = []
        for i in range(self.__rows):
            for j in range(self.__cols):
                tmp.append(0)
            main.append(tmp)
            tmp = []
        self.__seats[id] = main

    def book_seats(self, id, seat_list):
        for pair in seat_list:
            self.__seats[id][pair[0]][pair[1]] = 1

    def valid_seat(self, id, row, col):
        if row > self.__rows or col > self.__cols or self.__seats[id][row][col] == 1:
            return False
        return True

    def view_show_list(self):
        for movie in self.__show_list:
            print(f'Id: {movie[0]}, Title: {movie[1]}, Premiering at: {movie[2]}.')

    def view_available_seats(self, id):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0:
                    print(f'({i + 1}, {j + 1})', end = ' ')
            print()

alibaba_cinema = Star_Cinema()
alpha = Hall(1, 5, 5)
alpha.entry_show(101, 'The Greatest Showman', '12/12/2012, 10:00 AM')
alpha.entry_show(102, 'The Lion King', '11/11/2011, 04:00 PM')
alibaba_cinema.entry_hall(alpha)

while True:
    print("1. View Current Movies' Collection")
    print("2. View Available Seats")
    print("3. Book a Movie Ticket")
    print("4. Exit")
    command = int(input())
    if command == 1:
        print('We currently have 1 hall. These movies are premiering- \n')
        alpha.view_show_list()
        print('\n\n')

    elif command == 2:
        while True:
            view_seat_id = int(input('The Id of the movie you want to view available seats of: '))
            if alpha.valid_show_id(view_seat_id):
                break
            else:
                print('Invalid input')
        alpha.view_available_seats(view_seat_id)
        print('\n\n')

    elif command == 3:
        while True:
            to_be_booked = int(input("Movie Id you wish to book: "))
            if alpha.valid_show_id(to_be_booked):
                break
            else:
                print('Invalid input')
        seat_list = []
        while True:
            row = int(input('Seat Row: '))
            col = int(input('Seat Col: '))
            if alpha.valid_seat(to_be_booked, row - 1, col - 1):
                break
            else:
                print('Seat either taken or invalid!')
        tmp_tuple = (row - 1, col - 1)
        seat_list.append(tmp_tuple)
        alpha.book_seats(to_be_booked, seat_list)
        print(f'Your seat has been booked successfully! Seat no. ({row}, {col})\n\n')

    else:
        break