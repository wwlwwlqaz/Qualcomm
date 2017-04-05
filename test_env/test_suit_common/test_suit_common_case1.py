import fs_wrapper
from case_utility import *
from qrd_shared.case import *
import settings.common as SC
from test_case_base import TestCaseBase

class test_suit_common_case1(TestCaseBase):
    def test_case_main(self,case_results):
        excute("UIOBJECT:[UISELECTOR:;"
                        "FUNCTION:1:description;"
                        "FUNCTION_ARGS:String:Apps;];"
               "FUNCTION:0:clickAndWaitForNewWindow;"
               )

        excute("UIOBJECT:[UISELECTOR:;"
                        "FUNCTION:1:text;"
                        "FUNCTION_ARGS:String:Apps;];"
               "FUNCTION:0:click;"
               )

        excute("UISCROLLABLE:[UISELECTOR:;"
                            "FUNCTION:1:scrollable;"
                            "FUNCTION_ARGS:boolean:true;];"
               "FUNCTION:0:setAsHorizontalList;"
               "FUNCTION:2:getChildByText;"
               "FUNCTION_ARGS:UiSelector:[UISELECTOR:;"
                                        "FUNCTION:1:className;"
                                        "FUNCTION_ARGS:String:android.widget.TextView;];"
               "FUNCTION_ARGS:String:Settings;"
               )

        excute("UIOBJECT:;"
               "FUNCTION:0:click;")