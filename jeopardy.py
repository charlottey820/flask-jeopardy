# import requests
# API_endpoint = "https://jservice.io/api/clues"
# API_query = "value=1000"
# API_url = API_endpoint + "?" + API_query
# r = requests.get(API_url)
# data = r.json()
# print(API_url)
import requests
import random

response = requests.get('http://jservice.io/api/clues?category=139').json()

def match_clue(user_input, answer):
    # random_question_number = random.randint(0,99)
    # print(response[random_question_number]["question"])
    # answer = input("What is...")
    # if answer.capitalize().strip("?,.!") == response[random_question_number]["answer"].capitalize().strip("?,.!"):
    #     print("Congratulations, that is correct!")
    # else:
    #     print("Sorry, the correct answer was: What is " + response[random_question_number]["answer"]+"?")
    if user_input.capitalize().strip("?,.!") == answer.capitalize().strip("?,.!"):
        # print("Congratulations, that is correct!")
        return "Congratulations, that is correct!"
    else:
        # print("Sorry, the correct answer was: What is " + response[random_question_number]["answer"]+"?")
        return "Sorry, the correct answer was: What is " + answer+"?"

# user_continue = True
# user_input_valid = False
# def does_user_continue(user_input):
#     if user_input.lower()=="y":
#         return True
#     elif user_input.lower()=="n":
#         print("Thank you for playing!")
#         return False
#     else:
#         user_input = input("Invalid input, please try again.")
# while user_continue:
#     match_clue()
#     user_input = input("Do you want to continue? (y/n)")
#     # user_continue = does_user_continue(user_input)
#     if user_input.lower()=="y":
#         user_continue = True
#     elif user_input.lower()=="n":
#         print("Thank you for playing!")
#         user_continue = False
#     else:
#         while user_input_valid==False:
#             if user_input.lower()=="y" or user_input.lower()=="n":
#                 user_input_valid=True
#             else:
#                 user_input = input("Invalid input, please try again.\nDo you want to continue? (y/n)")
#                 print(user_input)
#                 if user_input.lower()=="y" or user_input.lower()=="n":
#                     user_input_valid==True
#                 print(user_input_valid)


# def magic(clue):
#     clue_category = clue["category"]["title"]
#     clue_value = clue["value"]
#     clue_question = clue["question"]
#     print(f"Category: {clue_category}")
#     print(f"Value: {clue_value}")
#     print(f"Question: {clue_question}")
# clue_one = data[5]
# magic(clue_one)