class Customer:
    def __init__(self, customer_id, customer_name):  # constructor with customer ID, name
        self.customer_id = customer_id
        self.customer_name = customer_name

    def get_id(self):
        return self.customer_id

    def get_name(self):
        return self.customer_name

    def display_info(self):
        # print customer info, with only basic fields for Customer
        print(f'ID: {self.customer_id}')
        print(f'Name: {self.customer_name}')
        print('Discount rate: na')
        print('Reward rate: na')
        print('Reward: na')

class Member(Customer):
    discount_rate = 0.1  # static/class variable for all Members

    def __init__(self, member_id, member_name):
        super().__init__(member_id, member_name)

    def get_discount_rate(self):
        return Member.discount_rate

    def get_discount(self, rental_cost):
        # Returns the discount value (not the cost after discount!)
        return rental_cost * Member.discount_rate

    def display_info(self):
        print(f'ID: {self.customer_id}')
        print(f'Name: {self.customer_name}')
        print(f'Discount rate: {Member.discount_rate * 100:.0f}%')
        print('Reward rate: na')
        print('Reward: na')

    @staticmethod
    def set_discount_rate(new_r):
        # static method to change the rate for all Members
        Member.discount_rate = new_r

class GoldMember(Member):
    discount_rate = 0.12  # static/class variable for all GoldMembers

    def __init__(self, gold_id, gold_name, reward_rate=1.0, reward=0):
        super().__init__(gold_id, gold_name)
        self.gold_reward_rate = float(reward_rate)
        self.gold_reward = int(reward)

    def get_discount_rate(self):
        return GoldMember.discount_rate

    def get_discount(self, rental_cost):
        return rental_cost * GoldMember.discount_rate

    def get_reward_rate(self):
        return self.gold_reward_rate
    
    def get_og_r(self):
        return self.gold_reward


    def get_reward(self, after_discount_cost):
        # Reward is rounded to nearest integer
        return round(after_discount_cost * self.gold_reward_rate)

    def update_reward(self, add_value):
        self.gold_reward += add_value

    def deduct_reward(self, minus_val):
        self.gold_reward -= minus_val

    def display_info(self):
        print(f'ID: {self.customer_id}')
        print(f'Name: {self.customer_name}')
        print(f'Discount rate: {GoldMember.discount_rate * 100:.0f}%')
        print(f'Reward rate: {self.gold_reward_rate * 100:.0f}%')
        print(f'Reward: {self.gold_reward}')

    @staticmethod
    def set_discount_rate(new_discount_rate):
        GoldMember.discount_rate = new_discount_rate

    def set_reward_rate(self, new_reward_rate):
        self.gold_reward_rate = new_reward_rate

class Book:
    def __init__(self, book_id, book_title, book_category=None, type= None):
        self.book_id = book_id
        self.book_title = book_title
        self.book_category = book_category
        self.type = type  

    def get_id(self):
        return self.book_id

    def get_name(self):
        return self.book_title

    def get_category(self):
        return self.book_category
    
    def set_category(self, category):
        self.book_category = category
    
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

    def get_price(self, days):
        if isinstance(self.book_category, BookCategory):
            return self.book_category.get_price(days)
        else:
            print('Error in self.book_category')

    def display_info(self):
        print(f'ID: {self.book_id}')
        print(f'Name: {self.book_title}')
        if isinstance(self.book_category, BookCategory):
            print(f'Category: {self.book_category.get_name()}')
        if isinstance(self.type, BookCategory):
            print(f'Type: {self.type.get_type_name()}')
        print('-'*40)


class BookCategory: 

    def __init__(self, category_id, category_name, category_type, price_1, price_2):
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type
        self.price_1 = float(price_1)
        self.price_2 = float(price_2)



        self.book_list = []  

    def get_id(self):
        return self.category_id

    def get_name(self):
        return self.category_name
    
    #add the getter method for category_type
    def get_type_name(self):
        return self.category_type
    
    def set_type(self, type):
        self.category_type = type
    
    def add_book(self, book_obj):
        self.book_list.append(book_obj)

    def pbpd(self, days):
        if int(days) <= 10:
            return  self.price_1
        else:
            return  self.price_2

    def get_price(self, days):
        # if days <=10 use price_1, else price_2
        if int(days) <= 10:
            return int(days) * self.price_1
        else:
            return int(days) * self.price_2
        

        
    #used for update cat info    
    def set_price_1(self, price_1):
        self.price_1 = price_1
    def set_price_2(self, price_2):
        self.price_2 = price_2



    def display_info(self):
        print(f'ID: {self.category_id}')
        print(f'Name: {self.category_name}')
        print(f'Type: {self.category_type}')
        print(f'Price 1: {self.price_1} AUD/day')
        print(f'Price 2: {self.price_2} AUD/day')


#CR bookseries class
class BookSeries:
    def __init__(self, series_id, series_name, comp_books, book_category = None, type= None):
        self.series_id = series_id
        self.series_name = series_name
        self.comp_books = comp_books
        self.book_category = book_category
        self.type = type
        
    def get_id(self):
        return self.series_id
    
    def get_name(self):
        return self.series_name
    
    def get_category(self):
        return self.book_category
    
    def set_category(self, category):
        self.book_category = category
    
    
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
    
    
    
    def get_original_price(self, days):
        pbpd = self.book_category.pbpd(days)
        total_books_in_series = len(self.comp_books)
        #create og_cost
        original_cost = pbpd * total_books_in_series * int(days)
        return original_cost
    
    def get_price(self, days):
        return 0.5 * self.get_original_price(days)
    
    def display_info(self):
        print(f'Series ID: {self.get_id()}')
        print(f'Series name: {self.get_name()}')

        
        for x in self.comp_books:
            if isinstance(x, Book):
                print(f'Component books: {x.get_name()}')

        if isinstance(self.get_category(), BookCategory):
            print(f'Category: {self.get_category().get_name()}')


        if isinstance(self.type, BookCategory):
            print(f'Type: {self.type.get_type_name()}')


        print('-'*40)

#PA:      
# so for class Rental, I thought about inheritance in Customer/Member/Goldmember,
# but I found this is logically wrong as rental is not a "type" of member/customer
# it is logically a standalone class that handles the rental

class Rental:
    def __init__(self, rental_customer, rental_book, rental_days):
        self.rental_customer = rental_customer
        self.rental_book = rental_book           
        self.rental_days = rental_days



    def compute_cost(self):


        #handling the og cost for series


        if isinstance(self.rental_book, BookSeries):
            original_cost = self.rental_book.get_price(self.rental_days)


        elif isinstance(self.rental_book, Book):
            original_cost = self.rental_book.get_price(self.rental_days)







        if isinstance(self.rental_customer, GoldMember):

            discount = self.rental_customer.get_discount(original_cost)

            total_cost = original_cost - discount


            # DI part, reward deduction
            old_rw = self.rental_customer.get_og_r()

            r_dct = 0

            m_dct = 0

            #every 20pts = 1$
            if old_rw >= 20:
                                #use floor divide to check how many 20s in old_rw

                r_dct = (old_rw // 20)*20


                m_dct = r_dct // 20 

                total_cost -= m_dct


                if isinstance(self.rental_customer, GoldMember):
                    self.rental_customer.deduct_reward(r_dct)  # update GoldMember's reward points

                    #debug
                else:
                    print(self.rental_customer)
                    print('Error in handling customer obj!')



            new_rw = self.rental_customer.get_reward(total_cost + m_dct)


            self.rental_customer.update_reward(new_rw)
            return (original_cost, discount, total_cost, new_rw, r_dct, m_dct)
#       ^
#       if goldmember...





        elif isinstance(self.rental_customer, Member):
            discount = self.rental_customer.get_discount(original_cost)
            total_cost = original_cost - discount
            return (original_cost, discount, total_cost, 0, 0, 0)
        

        else:#customer belongs to Customer
            return (original_cost, 0, original_cost, 0, 0, 0)


#After spending days to develop this following block of code,
#I realize that this OOP programming is really different from what I did in Assignment 1.
#The presence of class is adds more complexity to the logic to me.
#As a beginner, OOP is challenging.

#I tend to use analogy for me to understand the concepts better:
#the class Records is like a converter machine,
#it converts the txt file outside and place then accordingly
#and store them and can later be fetched
#so the design logic of this class should be like:
#1. I have to create containers (lists) to fill these outside information (txt files)
#2. Then convert these outside information to the internal classes (find methods)

class Records:
    def __init__(self):
        self.customer_list = []        #Customer and Customer related objects
        self.category_list = []        #BookCategory
        self.book_list = []            #Book 
        self.series_list = []          #BookSeriees objects

#HD     list to store rentals
        self.all_trsc = []


    def add_transaction_info(self, obj):
        self.all_trsc.append(obj)



    def display_all_rentals(self):
        for cus_obj, (b_and_d), total_original_cost, discount, total_cost, new_rw, timestamp in self.all_trsc:
            if not isinstance(cus_obj, GoldMember):
                new_rw = 'N/A'
            else:
                pass
            print('-'*50)
            print(f'Customer: {cus_obj.get_name()}')
            print('-'*50)
            for i in b_and_d:
                bn = i[0]
                bd = i[1]
                if isinstance(bn, Book):
                    print(f'Books and days: {(bn.get_name().strip() or bn.get_id().strip, bd)}')

                elif isinstance(bn, BookSeries):
                    print(f'Books and days: {(bn.get_name().strip() or bn.get_id().strip, bd)}')


            print('\n' + '-' * 50)
            print(f'Original cost:          {total_original_cost}')
            
            print(f'Discount:               {discount}')
            
            print(f'Amount Payable:         {total_cost}')
            
            print(f'Reward earned:          {new_rw}')
            
            print(f'Timestamp:       {timestamp}')
            print( '-' * 50)


#HD v.
    def get_all_transaction(self):
        return self.all_trsc



    def read_customers(self, customer_filename):
        with open(customer_filename, 'r') as file:
            line = file.readline()
            #because of .readline(), a while loop is preferred.
            # create a while loop to read the information in customer.txt
            while line:
                info = line.strip().split(',')
                customer_type = info[0]
                customer_id = info[1].strip()
                customer_name = info[2].strip()
                discount_rate = info[3].strip()
                reward_rate = info[4].strip()
                reward = info[5].strip()

                # using if-elif-else to filter the type of customer types 
                if customer_type == 'C':
                    customer_obj = Customer(customer_id, customer_name)
                    self.customer_list.append(customer_obj)

                elif customer_type == 'M':
                    customer_obj = Member(customer_id, customer_name)
                    self.customer_list.append(customer_obj)

                elif customer_type == 'G':
                    # handling the 'na' in reward rate and reward
                    rr = float(reward_rate) if reward_rate != 'na' else 1.0
                    rw = int(reward) if reward != 'na' else 0
                    customer_obj = GoldMember(customer_id, customer_name, rr, rw)
                    self.customer_list.append(customer_obj)


                line = file.readline()


    def read_books_and_book_categories(self, books_filename, category_filename):
        #book.txt
        with open(books_filename, 'r') as file:
            #CR:
            #I change readline into readlines for an easier code writing and clearer logic
            #because of .readlines(), a for loop could be used instead of while loop

            all_lines = file.readlines()

            #handle single books
            for line in all_lines:
                line = line.strip()
                if line.startswith("S"):  # skip series lines in this loop  
                    #reference:https://www.w3schools.com/python/ref_keyword_continue.asp
                    continue
                info = line.split(',')
                book_id = info[0]
                book_title = info[1]
                book_obj = Book(book_id, book_title)
                self.book_list.append(book_obj)

            # handle series
            for line in all_lines:
                line = line.strip()
                if line.startswith("S"):
                    info = line.split(',')
                    s_id = info[0].strip()
                    s_name = info[1].strip()

                    #handle component books in a series
                    book_names = []
                    
                    #book_names = info [2:]
                    #this ^ not working.
                    #so:

                    for name in info[2:]:
                        cleaned_name = name.strip()
                        book_names.append(cleaned_name)

                    comp_books_obj = []
                    for n in book_names:
                        book_obj = self.find_book(n)
                        if isinstance(book_obj,Book):
                            comp_books_obj.append(book_obj)
                        else:
                            print(f"Error: Book '{n}' not found for series '{s_name}'")
                    series_obj = BookSeries(s_id, s_name, comp_books_obj)
                    self.series_list.append(series_obj)

        #book_category.txt
        with open(category_filename, 'r') as file_1:
            line_1 = file_1.readline()
            while line_1:
                info_1 = line_1.strip().split(',')
                category_id = info_1[0].strip()
                category_name = info_1[1].strip()
                category_type = info_1[2].strip()
                price_1 = float(info_1[3])
                price_2 = float(info_1[4])

                #because series also needs signing to a category
                book_names = info_1[5:]
                                                                        
                category_obj = BookCategory(category_id, category_name, category_type, price_1, price_2)

                self.category_list.append(category_obj)
                
                #bc still category=None, type= None
                #so:
                for i in book_names:
                    book_obj = self.find_book(i.strip())
                    if isinstance(book_obj, Book):#book
                        book_obj.set_category(category_obj)
                        book_obj.set_type(category_obj) 
                        category_obj.add_book(book_obj) 
                    else: #series
                        series_obj = self.find_series(i.strip())
                        if isinstance(series_obj,BookSeries):
                            series_obj.set_category(category_obj)
                            series_obj.set_type(category_obj)
                
                
      
                line_1 = file_1.readline()
        



    # simple three for loops for search customer, category and book.
    def find_customer(self, search_value):
        for customer_obj in self.customer_list:
            #use .get_id method in class Customer
            if (customer_obj.get_id() == search_value.strip() or customer_obj.get_name().strip().lower() == search_value.strip().lower()):
                return customer_obj
            



    def find_book_category(self, search_value):
        for category_obj in self.category_list:
            #use .get_id method in class BookCategory
            if (category_obj.get_id().lower() == search_value.strip().lower() or category_obj.get_name().strip().lower() == search_value.strip().lower()):
                return category_obj



    def find_book(self, search_value):
        search_value = search_value.strip().lower()
        for book_obj in self.book_list:
            #use .get_id metod in class Book
            if (book_obj.get_id().strip().lower() == search_value or 
                book_obj.get_name().strip().lower() == search_value):
                return book_obj
            


    
    #series finder 
    def find_series(self, search_value):
        search_value = search_value.strip().lower()
        for series_obj in self.series_list:
            if (series_obj.get_id().strip().lower() == search_value or 
                series_obj.get_name().lower().strip() == search_value.strip().lower()):
                return series_obj
            



    # list info, use a for loop to make sure all the items in the list are included.
    def list_customers(self):
        print('-' * 50)
        for x in self.customer_list:
            x.display_info()
            print('-' * 50)

    def list_books(self):
        print('-' * 50)
        for x in self.book_list:
            x.display_info()
            print('-' * 50)

    def list_book_categories(self):
        print('-' * 50)
        for category_obj in self.category_list:
            category_obj.display_info() 
            print('-' * 50)   
    #update the list method to display info of book_series
    
    def list_books_and_book_series(self):
        print('-' * 50)

#list single books
        for book_obj in self.book_list:
            book_obj.display_info()
            print('-'*40)
#list series
#ID,name,compbook(iterative),category
        for series_obj in self.series_list:
            series_obj.display_info()
            print('-'*40)






#from my first assignment code, I borrowed the logic in error handling for update info methods,
#however, the structure is totally different because of the OOP structure.

#Note to myself for this section:
#the idea of object acts as an extra layer of protection for the original variable in OOP
#so everytime I wanted instinctly use the local variable I've created like category_name,
#In OOP, I always have to use a method and return an object so that the program can work properly
#and to fulfill the purpose of OOP
#a getter method is better for understanding this concept 


#while loop until input all verified as True(correct)
    #format
    #category name
    #type name
    #price number

    def update_info_of_a_category(self):
        valid_input = False
        
        while not valid_input:
            # Get user input
            update = input('To update information, please enter in the following format: "<category>, <type>, <price1>, <price2>" (separated by commas): ').strip()
            details = []
            for d in update.split(','):
                details.append(d.strip())
            



            #error handling
            if len(details) != 4:
                print('Error: Please enter exactly 4 values separated by commas.')
                continue 



            
            #assign the iems in the list details    
            category_name = details[0]
            category_type = details[1]  
            price_1 = details[2]
            price_2 = details[3]

            



            category_obj = self.find_book_category(category_name)
            if not isinstance(category_obj, BookCategory):
                print(f'Error: Category <{category_name}> not found.')
                continue
                


            
            if category_type.lower() not in ['rental', 'reference']:
                print('Error: Type must be either <rental> or <reference>.')
                continue
                



            # Validate prices
            try:
                price1 = float(price_1)
                price2 = float(price_2)
                if price1 <= 0 or price2 <= 0:
                    print('Error: Prices must be positive numbers.')
                    continue
            except ValueError:
                print('Error: Prices must be valid numbers.')
                continue
                



            # All validations passed - update category
            if isinstance(category_obj, BookCategory):
                if category_type.islower():
                    category_type = category_type.capitalize()
                    
                category_obj.set_type(category_type)
                category_obj.set_price_1(price1)
                category_obj.set_price_2(price2)

            if category_name.islower():
                category_name = category_type.capitalize()
            print( '-'* 50)
            print(f'\nSuccessfully updated category <{category_name}>:')
            print(f'Type:        {category_obj.get_type_name()}')
            print(f'Price 1:     {price1} AUD/day')
            print(f'Price 2:     {price2} AUD/day')
            print( '\n','-'* 50)
            valid_input = True


#also, borrowed from my first assignment logic:
            
#logic flow of the update books of a category
#asks user to choose <a/r>
#handling invalid input of choice
#proceed to corresponding functions
#asks user to input in the required format to proceed add/remove operation
#check if the input itself follows the format
#check if the input already exists for add operation, if exists, do nothing and report error to user
#check if the input non-exists for remove operation, if non-exist, do nothing and report error to user.
#if add/remove condition is met, proceed to add/remove function
#a feedback print that items has been successfully added/removed

    def update_books_of_a_category(self):





        #a/r handling
        valid_action = False
        while not valid_action:
            action = input('Enter <a/r> to add or remove books from category: ').strip().lower()
            if action != 'a' and action != 'r':
                print('Enter <ar> or <r> only to proceed!')
                continue
            else:
                valid_action = True






        #input handling
        valid_input = False
        while not valid_input:
            #Get input
            update = input('Enter in format: <category>, <book_1:book_1_ID>, <book_2:book_2_ID>, ...: ').strip()
            
            details = [item.strip() for item in update.split(',')]

          
            if len(details) < 2:
                print('Format error: Please enter category name and at least one book/series.')
                continue

            category_name = details[0]
            category_obj = self.find_book_category(category_name)
            if not isinstance(category_obj, BookCategory):
                print(f'Error: Category <{category_name}> not found.')
                continue




            
            #I designed a counter helps to later to print how many items processed

            processed_count = 0     


            for i in details[1:]:
                if ':' not in i:
                    print(f'Invalid input <{i}>! Follow: <book_1:book_1_ID>')
                    continue

                bn_bid = []
                for item in i.split(':'):
                    bn_bid.append(item)

                print(f'for {bn_bid}: ')


                #pair-pair array
                for i in range(0, len(bn_bid), 2):
                    
                    name = bn_bid[i]

                    id_val = bn_bid[i+1]



                                
                #work as True/false checker for all the conditions given
                #reference: https://docs.python.org/3/library/stdtypes.html Boolean Operations
                    item = (self.find_series(id_val)
                            or self.find_series(name)
                            or self.find_book(id_val)
                            or self.find_book(name)
                        )
                    


    
                    #add handle

                if action == 'a'and item:
                    print(f'Book/Series <{name}:{id_val}> already exists!')
                    continue




                elif action == 'a' and not item:
                    #designed another input choice for distinguish series or books
                    bk_or_sr = input(f'Is <{name}:{id_val}> a <book> or <series>? <b> for book, <s> for series. (caps insensitive): ').strip().lower()
                    if bk_or_sr == 'b':
                        new_book = Book(id_val, name)
                        self.book_list.append(new_book)
                        new_book.set_category(category_obj)
                        print(f'Successfully added <{name}:{id_val}> as a Book')
                        processed_count += 1
                        valid_input = True





                    elif bk_or_sr == 's':
                        #another while loop bc to handle component books
                        v = False
                        while not v:    
                            comp_book = input(f'Enter the component book of <{name}> series, <book_1:book_1_ID> , <book_2:book_2_ID> (caps sensitive): ').strip()
                            
                            cb = [] #for BookSeries

                            for b in comp_book.split(','):
                                if ':' not in b:
                                    print(f'Invalid input <{b}>! Follow: <book_1:book_1_ID>')

                                    v=False
                             
                                else:
#breakdown comma, check if colon > breakdown colon >
#assign BKobj> store to cb > add all to BKSRS > set methods
                                        
                                        temp = []
                                        for x in b.split(':'):
                                            temp.append(x)
                                        
                                        cbname = temp[0]
                                        cbid_val = temp[1]



                                        b_obj = Book(cbid_val, cbname)
                                        self.book_list.append(b_obj)
                                        b_obj.set_category(category_obj)
                                        cb.append(b_obj)

                                        print(f'Successfully added <{cbname}:{cbid_val}> as component book')


                            new_sr = BookSeries(id_val, name, cb)
                            self.series_list.append(new_sr)
                            new_sr.set_category(category_obj)
                            new_sr.set_type(category_obj)
                            print(f'Successfully added <{name}:{id_val}> as a Series')
                            processed_count += 1
                            valid_input = True

                            v=True









                    
                    #remove


                if action == 'r' and not item:
                    print(f'You are trying to remove an non-existing <{name}> book/series!')
                    continue




                elif action =='r' and item:
                    if isinstance(item, Book):
                        category_obj.book_list.remove(item)
                        self.book_list.remove(item)
                        item.set_category(None)
                        processed_count += 1
                        print(f'Successfully removed Book <{name}:{id_val}>!')
                        valid_input = True


                    elif isinstance(item, BookSeries):
                        item.set_category(None)
                        self.series_list.remove(item)
                        processed_count += 1
                        print(f'Successfully removed BookSeries <{name}:{id_val}>!')
                        valid_input = True
            
#           ^
#        for [1:]

            if processed_count > 0:
                action_word = 'added' if action == 'a' else 'removed'
                print(f'Successfully {action_word} {processed_count} item(s) to/from category.')
            else:
                print('Error: No items were processed.')       
        




    # a method to add new customers to customer_list[] 
    def add_customer(self, customer_obj):
        self.customer_list.append(customer_obj)

#required exceptions
    
class InvalidCustomerNameError(Exception):
    pass

class InvalidBookError(Exception):
    pass

class InvalidBorrowDaysError(Exception):
    pass

class ReferenceBookBorrowLimitError(Exception):
    pass

class Operations:
    def __init__(self):
        self.records_obj = Records()
        # try-except structure to raise exception if the files are corrupted and exit the program
        try:



            self.records_obj.read_customers('customers.txt')
            print('<customers.txt> read successful')
            self.records_obj.read_books_and_book_categories('books.txt', 'book_categories.txt')
            print('<books.txt> and <book_categories.txt> read successful')



            
        except FileNotFoundError as e:
            print(e)
            print('Program will now exit...')
            exit()





    # menu display method
    def display_menu(self):
        print("1. Rent a book")
        print("2. Display existing customers")
        print("3. Display existing book categories")
        print("4. Display existing books")
        print("5. Update information of a category")
        print("6. Update books of a category")
        print("7. Adjust the discount rate of all members")
        print("8. Adjust the reward rate of a Gold member")
        print("9. Rent books via a file")
        print("10. Display all rentals")
        print("11. Display most valuable customer")
        print("00. Exit Program")





#rent_book logic flow:
#name , valid, book/series, valid, days, valid, calculate costs.

    def rent_book(self):


        #user name has exception limit only alphabetical
        #thus i created a selection to input name or id before taking the input
        valid_select = False
        while not valid_select:
            select = input('Search customer by <ID> or <Name>? (enter <i> or <n> to proceed): ').strip().lower()
            if select == 'n' or select == 'i':
                valid_select = True
            else:
                print('Enter <i> for ID entry option or <n> for name entry option! (i/n)')
                continue






#CUSTOMER input exception
        valid_customer_input = False
        while not valid_customer_input:
        # take in customer name
            if select == 'n':
                input_customer_name = input('Enter customer name: ').strip()
                # try-exception to raise CustomerNameError
                try:
                    if not input_customer_name.replace(' ','').isalpha():
                        raise InvalidCustomerNameError('Alphabet character for names only!')
                    else:
                        search_value = input_customer_name
                        valid_customer_input = True
                #catch the error
                except InvalidCustomerNameError as e:
                    print(e)
    
            elif select == 'i':
                input_customer_id = input('Enter customer ID: ').strip()
                try:
                    if not input_customer_id.isnumeric():
                        raise InvalidCustomerNameError('Numbers only!')
                    else:
                        search_value = input_customer_id
                        valid_customer_input = True
                except InvalidCustomerNameError as e:
                    print(e)
            
    #   ^
    #   while not v_c_i
        fc = self.records_obj.find_customer(search_value)
        
        if fc == None:
            #a temp info for new customer
            fc = Customer(0000,search_value)
        
#name finish

                    
        



        
        conclusion = []
        rent_another_book = True




#logic flow DI i.
#1rent anohter book loop
    #2 rent book method
    #3 'y/n' = continue/end loop


#1
        while rent_another_book:
            

#BOOK/SERIES input error handling
#2
            valid_input_found = False
            while not valid_input_found:
                input_book_title = input('Enter name/series of the book rented: ').strip()

                try:
                    found_book_obj = self.records_obj.find_book(input_book_title)

                    found_series_obj = self.records_obj.find_series(input_book_title)



                    if not found_book_obj and not found_series_obj:
                        #raise the error
                        raise InvalidBookError("Book/Series not found. Please enter a valid book name.")
                    
                    elif found_book_obj and found_book_obj.get_type().get_type_name().strip() == 'Reference':
                        print(f'{input_book_title} is limited to 14 days of borrowing max.')
                        valid_input_found = True
    
                    else:
                        valid_input_found = True


                #catch the error
                except InvalidBookError as e:
                    print(f"Error: {e}")




            #avoid 2nd round error, always update
            fbs = found_book_obj or found_series_obj
#book finish





#DAYS exception
            valid_days = False
            while not valid_days:
                try:
                    days = int(input('Enter number of borrowing day(s): '))


                    if days <= 0:
                        raise InvalidBorrowDaysError('Borrowing days must be positive')
                    


                    elif fbs.get_type().get_type_name().strip() == 'Reference' and days > 14:
                        raise ReferenceBookBorrowLimitError('Reference type limit: no more than 14 days.')


                    else:
                        valid_days = True

                #a value error handle the non-integer values
                except ValueError:
                    print('Enter correct integer for days!')
                #Catches the error
                except InvalidBorrowDaysError as e:
                    print(e)
                except ReferenceBookBorrowLimitError as e:
                    print(e)
#days finish






            rental_obj = Rental(fc, fbs, days)

            cost = rental_obj.compute_cost()

            conclusion.append((fbs, days, cost))#store the items as tuples
            
#calculate finish




#3
            valid_answer = False
            while not valid_answer:
                answer = input('Rent another book/series? (y/n): ').strip().lower()
                if answer == 'n':
                    rent_another_book = False  # Exit outer loop
                    valid_answer = True
                elif answer == 'y':
                    valid_answer = True  # Continue loop
                else:
                    print('Invalid input. Please enter "y" for yes or "n" for no.')


    #   ^
    #   while rent_another










        self.display_receipt(fc, conclusion)


        #add new cus
        if (isinstance(fc, Customer) and fc.get_id() == 0000) or (fc.get_id() == None):
            
            print(f'Customer <{search_value}> is a new customer.')


            try:
                if fc.get_id() == 0000 and not search_value.isnumeric:
                    id = int(input(f'Assign an ID for <{search_value}>: '))
                elif search_value.isnumeric:
                    id = search_value
                    print(f'New ID has {search_value} has been updated')
                    input_customer_name = int(input(f'Enter the <customer name> of <{search_value}>: '))
            except ValueError as e:
                print(e)
                
            v = False
            while not v:

                choice = input('Add to Member class? <y/n>: ').strip().lower()

                if choice != 'y' and choice != 'n':
                    print('Enter <y> or <n> to proceed')

                elif choice == 'y':
                   
                    fc = Member(id, input_customer_name)

                    self.records_obj.add_customer(fc)
                    print(f'Successfully added <{search_value}> to Member class!')
                    print('-'*50)
                    v=True
                elif choice =='n':
                    
                    fc = Customer(id, input_customer_name)
                    self.records_obj.add_customer(fc)
                    print(f'Keep <{search_value}> as Customer class')
                    print('-'*50)
                    v= True







#receipt
    def display_receipt(self, customer_obj, conclusion):
        print('\n' + '-' * 50)
        print(f'Receipt for {customer_obj.get_name()}')
        print('-' * 50)

        total_original_cost = 0
        total_discount = 0

        total_final_cost = 0


        #DI part
        total_new_rw = 0

        total_points_deducted = 0

        total_money_deducted = 0.0

#DI Part:


        for fbs, days, cost in conclusion:
            if isinstance(fbs, (Book, BookSeries)):
                book_category = fbs.get_category()
#finish unpack



        #CR Part    
        # for the receipt section, the bookseries/book difference should also be handled



            if isinstance(fbs, BookSeries):

                #receipt part for series
                pbpd = book_category.pbpd(days)
                total_books = len(fbs.comp_books)
                print(f'Books rented:')
                print(f'- {fbs.get_name()} <series> for {days} days ({(pbpd * total_books):.2f} AUD/day)')
                print('-' * 50)
                print(f'Number of books:     {total_books}')
                print('-'*50)



            elif isinstance(fbs, Book): #a single book
                if int(days) <= 10:
                    ppd = book_category.price_1
                else:
                    ppd = book_category.price_2

                #receipt part for all kind of customers
                print(f'Books rented:')
                print(f'- {fbs.get_name()} for {days} days ({ppd} AUD/day)')
                print('-' * 50)
#finish iterate book receipt



            
            # DI, managing cost and print receipt
            if isinstance(customer_obj, GoldMember):

                original_cost = float(cost[0])
                discount = float(cost[1])
                total_cost = float(cost[2])
                new_rw = float(cost[3])
                r_dct = int(cost[4])
                m_dct = int(cost[5])


                total_new_rw += new_rw

                total_points_deducted += r_dct

                total_money_deducted += m_dct

                final_reward_points = customer_obj.gold_reward


            else:
                original_cost = float(cost[0])
                discount = float(cost[1])
                total_cost = float(cost[2])
                


            total_original_cost += original_cost

            total_discount += discount
            total_final_cost += total_cost
#finish iterate calculation

#       ^
#       for x,y,z in conclusion


        print(f'Original Cost:       {total_original_cost:.2f} (AUD)')
        print(f'Discount:            {total_discount:.2f} (AUD)')




        if isinstance(customer_obj, GoldMember):
            if total_points_deducted >= 20:
                print(f'Reward point used:   {total_points_deducted}')

                print(f'Money deducted:      {total_money_deducted:.2f} (AUD)')

            print(f'Amount payable:      {total_final_cost:.2f} (AUD)')

            print(f'Reward earned:       {total_new_rw}')

            print(f'Reward balance:      {final_reward_points}')




        else:
            print(f'Amount payable:      {total_final_cost:.2f} (AUD)')
        print('-' * 50)
            
#finish type specific receipt

#HD i., ref:https://docs.python.org/3/library/datetime.html

        import datetime
        time = datetime.datetime.now()
        timestamp = time.strftime("%d/%m/%Y %H:%M:%S") 




#HD iii. copypaste from what I wrote in HD ii.
        info = (customer_obj if customer_obj.get_id()!= 0000 else f'1st time-customer {customer_obj}',



                ((bid_ds, days) for bid_ds, days, cost in conclusion),



                total_original_cost, discount, total_cost, 
                new_rw if isinstance(customer_obj, GoldMember) else 'na', 
                timestamp
            
        )

        self.records_obj.add_transaction_info(info)








    
    #DI, adjust discount rate

    def adjust_discount_rate(self):


        valid_input = False
        while not valid_input:

            try:
                new_r = input('Enter the new discount rate (e.g., 0.2 for 20%): ').strip()

                        #handle non-number
                new_r = float(new_r)

                        #handle negative, 0
                if new_r <= 0:
                    raise ValueError('Discount rate must be a positive number!')
                else:
                    Member.set_discount_rate(new_r)
                    GoldMember.set_discount_rate(new_r)

                print(f'Successfully updated discount rate for all members to {new_r * 100:.0f}%')

                valid_input = True
            except ValueError as e:
                print(e)






    #Di, golmember rr
    def adjust_gold_member_reward_rate(self):


        #handle invalid customer
        valid_customer = False
        while not valid_customer:
            try:

                cus = input('Enter the ID or Name of the Gold Member: ').strip()

                cus_obj = self.records_obj.find_customer(cus)


                if not cus_obj or not isinstance(cus_obj, GoldMember):

                    raise InvalidCustomerNameError('Customer not found!')
                
                elif cus_obj and isinstance(cus_obj,GoldMember):
                    print(f'Customer {cus} found!')
                    valid_customer = True

            except InvalidCustomerNameError as e:
                print(e)
            except InvalidCustomerNameError as e:
                    print(e)
        
        #handle invalid rate

        valid_rate = False
        while not valid_rate:
            try:
                
                new_rr = input(f'Enter the new reward rate for {cus}(current rate={cus_obj.get_reward_rate()}) (e.g., 0.2 for 20%): ')
                #handle non-number
                new_rr = float(new_rr)

                if new_rr <= 0:
                    raise ValueError('Reward rate must be positive!')
                
                else:
                    cus_obj.set_reward_rate(new_rr)
                    print(f"Successfully set {cus}'s reward rate to {new_rr*100}%")
                    valid_rate = True


            except ValueError as e:
                print(e)







#HD ii:
    def rent_books_via_a_file(self):
        try:
            f_name = input('Enter the username (caps sensitive): ').strip()
            with open(f_name ,'r') as file:
                all_lines = file.readlines()

                for line in all_lines:


                    detail = line.strip().split(',')

                    cus = detail[0]

                    cus_obj = self.records_obj.find_customer(cus)
                    
                    templist=[]

                    for i in range(1, len(detail) - 5, 2):
                        bid_bn = detail[i]

                        b_s_obj = self.records_obj.find_series(bid_bn) or self.records_obj.find_book(bid_bn) 

                        day = detail[i+1]
                        
                        
                        templist.append((b_s_obj, day))
                
                
                    og_cost = float(detail[-5])
                    discount = float(detail[-4])
                    total_cost = float(detail[-3])
                    earned_r = float(detail[-2]) if detail[-2].isnumeric() else 0
                    date = detail[-1].strip()

                    if isinstance(cus_obj, GoldMember):
                        cus_obj.update_reward(earned_r)

            
                    info = (
                        
                        cus_obj if cus_obj.get_id()!= 0000 else f'1st time-customer {cus}',

                        
                        
                        templist,



                        og_cost, discount, total_cost, 
                        earned_r if isinstance(cus_obj, GoldMember) else 'na', 
                        date
                    
                    )

                    self.records_obj.add_transaction_info(info)
#       ^   ^
#     try   with open...
        except FileNotFoundError:
            print("Cannot find the rental file.")

###I am very proud of myself after wrtiing this complicated code.
#Throughout this coding project, it reflects how I am constantly improving and familiarizing with
#coding in general.

#It's actually amazing to see how I did differently in PA, CR and DI, HD parts
#Honestly, I myself couldn't even believe I was capable to write all these code just a few months ago.
# The feeling of accomplishment keeps driving me to learn more, I really enjoyed it!









#HD iii:
    def display_all_rentals(self):
        
        self.records_obj.display_all_rentals()


#HD v.
    def display_vip(self):
        #a dictionary better to retrieve the spending and customer
        store = {}
        for cus, (b_and_d), total_original_cost, discount, total_cost, new_rw, timestamp in self.records_obj.get_all_transaction():
            store[f'{cus.get_name()}'] = total_cost
        
        #ref:https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
        vip_n = max(store, key=store.get)
        vip_s = store.get(vip_n)
        print('\n' + '-' * 50)
        print(f'VIP customer:     {vip_n}')
        print(f'Total spending:   {vip_s}')
        print( '-' * 50)
        

        



            










    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.rent_book()
            elif choice == '2':
                self.records_obj.list_customers()
            elif choice == '3':
                self.records_obj.list_book_categories()
            elif choice == '4':
                self.records_obj.list_books_and_book_series()
            elif choice == '5':
                self. records_obj.update_info_of_a_category()
            elif choice == '6':
                self.records_obj.update_books_of_a_category()
            elif choice == '7':
                self.adjust_discount_rate()
            elif choice == '8':
                self.adjust_gold_member_reward_rate()
            elif choice == '9':
                self.rent_books_via_a_file()
            elif choice == '10':
                self.display_all_rentals()
            elif choice =='11':
                self.display_vip()
            elif choice == '00':     
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter a valid choice!")



#HD iv: reference:https://docs.python.org/3/library/argparse.html
import sys

customer_file = "customers.txt"
book_file = "books.txt"
category_file = "book_categories.txt"






op = Operations()
op.run()
