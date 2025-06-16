import time
import os
import praw  # Reddit's API wrapper, for the bot itself


def fill_comment(str_in):  # pads length of string by repeating string
    # print(f"check length A:  {len(str_in)}") # vestigal line used in testing
    target_length = 10000  # limit of comment length
    times = target_length // len(str_in)
    # print(f"times:  {times}")                # vestigal line used in testing
    str_in = str_in * times
    remainder = target_length - len(str_in)
    # print(f"check length B:  {len(str_in)}") # vestigal line used in testing
    str_in += (" ") * (remainder - times)
    # print(f"check length C:  {len(str_in)}") # vestigal line used in testing
    return str_in


def main():
    string = (
        "placeholder string"
    )
    comment_string = fill_comment(string)  # pads string used for overwriting comments
    str_list = ["[deleted]", "[removed]"]  # avoid overwriting deleted or removed comments
    reddit = praw.Reddit(     # python wrapper for reddit
        client_id=     "dummy string", # replace dummy strings with desired values
        client_secret= "dummy string",
        password=      "dummy string",
        user_agent=    "dummy string",
        username=      "dummy string",
    )
    reddit.validate_on_submit = True
    print("")
    print("")
    id_list = []
    f = open("comments.txt", "r") # file containing comment IDs to be edited
    """
    The file comments.txt should contain a list of comment IDs, one per line.
    IDs can be obtained from Reddit data request file "comments.csv".
    """
    for line in f:
        id_list.append(line.strip())
    f.close()
    index = 0 # list index to start at
    number = 101 # number of comment_IDs to process
    id_list = id_list[index - 1 :] # slice list to start at index
    count = index - 1
    for id in id_list:
        count += 1
        print(f"{count:03} id: {id}", end="")
        try:
            comment = reddit.comment(id)
            copy = str(comment.body)
        except:
            print(" exception caught :D")  # print newline when there is an exception
            continue
        else:
            print(f', length: {len(copy):4} body: "{copy[:41]:42}", ', end="")
            if copy in str_list:
                print("removed or deleted")
                continue
            if len(copy) > 9000:
                if copy[:41] == comment_string[:41]:
                    print("already edited")
                    continue
            comment.edit(comment_string)
            print("edit attempted")


if __name__ == "__main__":
    main()
