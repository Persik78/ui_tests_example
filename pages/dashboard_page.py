import allure
from base.base import Base
from config.links import Links

class DashboardPage(Base):

    #Locators
    title_dashboard_page = '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]'

    #Getters
    def get_title_dashboard_page(self):
        return self.find_element_of_presence(self.title_dashboard_page)


    #Actions


    #Methods
    @allure.step('Checking title dashboard page')
    def check_title_dashboard_page(self):
        self.soft_assert_url(Links.DASHBOARD_PAGE)
        self.soft_assert_word(self.get_title_dashboard_page(), 'Dashboard')
        self.get_screenshoot()