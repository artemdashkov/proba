
def check_language(cur_language):
    if cur_language not in ["hu", "nl", "el"]:
        return
    print(f"This test is not for {cur_language} language")

