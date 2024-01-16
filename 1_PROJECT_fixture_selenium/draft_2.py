@allure.step('Start test "Click 2 from 5 random [Sell] buttons in "CFDs tables" for {type_fi} and {tab}')
def test_05_cfd_table_button_sell_tab(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
        cur_type_fi, cur_tab):
    """
    Check: Button [1. Sell] in block "CFDs table" in {cur _tab} tab
    Language: All. License: All.
    """
    build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                         "11.01.03", "Educations > Menu item [CFD trading guide]",
                         ".01_05", f"Testing 2 random buttons [Sell] in {cur_type_fi} table "
                                   f"and in {cur_tab} tab")

    Common().check_language_in_list_and_skip_if_not_present(
        cur_language, ["", "de", "es", "nl", "pl", "ro", "ru", "zh"])
    check_cur_href(cur_item_link, cfd_markets_href)

    page_conditions = Conditions(d, "")
    page_conditions.preconditions(
        d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

    test_element = SellButtonTable(d, cur_item_link)
    test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link, cur_type_fi, cur_tab)