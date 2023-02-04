from application.salary import calculate_salary as salary_calc
from application.db.people import get_employees
from datetime import date
import emoji


def print_current_date():
    print(f'Today {date.today().strftime("%d %B %Y")}')


if __name__ == '__main__':
    print_current_date()
    salary_calc()
    get_employees()

    # https: // www.webfx.com / tools / emoji - cheat - sheet /
    print(emoji.emojize('Python is :thumbs_up:'))

    print('Example other emoji:')
    emoji_list = [
        ':thumbs_down:',
        ':rolling_on_the_floor_laughing:',
        ':winking_face:',
        ':red_heart:',
        ':grinning_face:',
        ':worried_face:'
    ]

    for el in emoji_list:
        print(emoji.emojize(el))