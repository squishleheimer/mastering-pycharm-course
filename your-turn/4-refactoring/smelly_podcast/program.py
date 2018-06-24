import random

from service import get_episode, get_latest_show_id, download_data


def main():
    show_header()

    download_data()

    print("Working with total of {} episodes".format(get_latest_show_id()))

    display_results()


def display_results():
    # DISPLAY RESULTS
    start = random.randint(90, 110)
    latest_id = get_latest_show_id()
    end = random.randint(130, latest_id + 1)
    for show_id in range(start, end):
        get_episode(show_id)


def show_header():
    # SHOW THE HEADER
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
