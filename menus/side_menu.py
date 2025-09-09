from base.base import Base


class SideMenu(Base):

    #Locators
    admin = '//span[text()= "Admin"]'
    pim = '//span[text()= "PIM"]'
    leave = '//span[text()= "Leave"]'
    time = '//span[text()= "Time"]'
    recruitment = '//span[text()= "Recruitment"]'
    my_info = '//span[text()= "My Info"]'
    performance = '//span[text()= "Performance"]'
    dashboard = '//span[text()= "Dashboard"]'
    directory = '//span[text()= "Directory"]'
    maintenance = '//span[text()= "Maintenance"]'
    claim = '//span[text()= "Claim"]'
    buzz = '//span[text()= "Buzz"]'


    #Getters
    def get_admin(self):
        return self.find_element_to_be_clickable(self.admin)
    def get_pim(self):
        return self.find_element_to_be_clickable(self.pim)
    def get_leave(self):
        return self.find_element_to_be_clickable(self.leave)
    def get_time(self):
        return self.find_element_to_be_clickable(self.time)
    def get_recruitment(self):
        return self.find_element_to_be_clickable(self.recruitment)
    def get_my_info(self):
        return self.find_element_to_be_clickable(self.my_info)
    def get_performance(self):
        return self.find_element_to_be_clickable(self.performance)
    def get_dashboard(self):
        return self.find_element_to_be_clickable(self.dashboard)
    def get_directory(self):
        return self.find_element_to_be_clickable(self.directory)
    def get_maintenance(self):
        return self.find_element_to_be_clickable(self.maintenance)
    def get_claim(self):
        return self.find_element_to_be_clickable(self.claim)
    def get_buzz(self):
        return self.find_element_to_be_clickable(self.buzz)


    #Actions

    def click_admin(self):
        self.get_admin().click()

    def click_pim(self):
        self.get_pim().click()

    def click_leave(self):
        self.get_leave().click()

    def click_time(self):
        self.get_time().click()

    def click_recruitment(self):
        self.get_recruitment().click()

    def click_my_info(self):
        self.get_my_info().click()

    def click_performance(self):
        self.get_performance().click()

    def click_dashboard(self):
        self.get_dashboard().click()

    def click_directory(self):
        self.get_directory().click()

    def click_maintenance(self):
        self.get_maintenance().click()

    def click_claim(self):
        self.get_claim().click()

    def click_buzz(self):
        self.get_buzz().click()


    #Methods