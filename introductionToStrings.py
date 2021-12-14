greeting = "Hello"
first_name = "James"
last_name = "Darwin"
white_space = ' '
exclamation_sign = '!'
whole_sentence = greeting + white_space + first_name + \
                 white_space + last_name + exclamation_sign
long_string = "This is a long string "
print(whole_sentence + white_space + long_string)
next_string = 'I want to learn\'Python\'!'
print(next_string)
string_new_line = "This is string wich will\n \rbe transferred."
print(string_new_line)
numbers = '1\t23456'
print(numbers)

song_txt_p1 = """Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full """
song_txt_p2 = "One for the master,\nOne for the dame,\n  \rAnd one for the little boy\n \rWho lives down the lane "
# Here in last string we use double tab
song_txt_p3 = "\n\rBaa, baa, black sheep,\nHave you any wool?\nYes sir, yes sir,\n\t\tThree bags full"
print(song_txt_p1 + song_txt_p2 + song_txt_p3)

first_name = 'Winston'
last_name = 'Churchill'
age = 50
print('Hi! my name is ' + first_name + ' ' + last_name \
      + 'I\'m' + ' ' + str(age) + ' ' + 'years old.')


