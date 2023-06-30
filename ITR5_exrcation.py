

import numpy as np
import pandas as pd
import json
def flatten_json(nested_json):
    """
    The function flattens a nested JSON object into a single-level dictionary.
    
    :param nested_json: a JSON object that may contain nested objects and arrays
    :return: The function `flatten_json` returns a flattened version of the input `nested_json`
    dictionary. The keys of the nested dictionary are concatenated with underscores to create a
    flattened key in the output dictionary. The output is a dictionary with the flattened keys and their
    corresponding values.
    """
    out = {}
    def flatten(x,name = ''):
        if type(x) is dict:
            for a in x:
                flatten(x[a],name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a,name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(nested_json)
    return out


##
def itr5_json_variable_extraction(t:dict):
    """
    The function extracts relevant information from a dictionary containing ITR5 form data and returns
    it in a flattened format.
    
    :param t: The input dictionary containing the parsed JSON data of an ITR form
    :type t: dict
    :return: The function itr5_json_variable_extraction returns a dictionary containing various
    extracted information from the input dictionary t, which is assumed to contain data related to an
    ITR5 form. The extracted information includes general ITR information, partner/member information,
    nature of business, manufacturing account details, trading account details, and PartA_PL details.
    """
    
    itr_dict={}
    itr_form_type='ITR5'
    itr_form='Form_ITR5'
    itr_kyes=t['ITR'][itr_form_type].keys()
    ##important tags ITR5
    # itr=['Form_ITR5', 'PartA_GEN1', 'PartA_GEN2', 'PARTA_BS', 'ManufacturingAccount', 'TradingAccount', 'PARTA_PL']

    ###extracted PartA_GEN
    itr_dict['itr_form']=t['ITR'][itr_form_type][itr_form]['FormName']
    itr_dict['assessmentyear']=t['ITR'][itr_form_type][itr_form]['AssessmentYear']

    ###general itr infomation
    itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN1']))
    # print(itr_dict)

    ###extracted PartA_GEN2
    # try:
    #     nat_bus=flatten_json((t['ITR'][itr_form_type]['PartA_GEN2']['NatOfBus']['NatureOfBusiness'][0]))
    #     itr_dict.update(nat_bus)
    # except:
    #     NatureOfBusiness_var = ['Code','TradeName1','Description']
    #     nat_bus={key:None for key in NatureOfBusiness_var}
    #     itr_dict.update(nat_bus)
    
    try:
        PartA_GEN2_keys = t['ITR'][itr_form_type]['PartA_GEN2'].keys()
        if 'PartnerOrMemberInfo' in PartA_GEN2_keys:

            PartnerOrMemberInfo=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2']['PartnerOrMemberInfo'])

            itr_dict['parterner_info']=PartnerOrMemberInfo

            del t['ITR'][itr_form_type]['PartA_GEN2']['PartnerOrMemberInfo']

        else:
            itr_dict['parterner_info']=np.nan
    except:
        pass
    try:
        nature_of_bus_keys=t['ITR'][itr_form_type]['PartA_GEN2']['NatOfBus'].keys()
        if 'NatureOfBusiness' in nature_of_bus_keys:

            NatureOfBusiness=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2']['NatOfBus']['NatureOfBusiness'])

            itr_dict['nature_of_business']=NatureOfBusiness

            del t['ITR'][itr_form_type]['PartA_GEN2']['NatOfBus']['NatureOfBusiness']

        else:
            itr_dict['nature_of_business']=np.nan
    except:
        pass
    
    itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN2']))


    ###'PARTA_BS'   
    for key in t['ITR'][itr_form_type]['PARTA_BS'].keys():

        itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PARTA_BS'][key]))

    ####ManufacturingAccount
    if 'ManufacturingAccount' in itr_kyes:
        ManufacturingAccount=flatten_json(t['ITR'][itr_form_type]['ManufacturingAccount'])
        # print(ManufacturingAccount)
        ManufacturingAccount['manufacturing_account']="found"
        itr_dict.update(ManufacturingAccount)

    else:
        ManufacturingAccount_var=['OpeningInventory_OpngStckRawMat', 'OpeningInventory_OpngStckWrkinPrgrs', 'OpeningInventory_OpngInvntryTotal',
         'OpeningInventory_Purchases', 'OpeningInventory_DirectWages', 'OpeningInventory_DirectExpenses', 'OpeningInventory_CarriageInward',
         'OpeningInventory_PowerAndFuel', 'OpeningInventory_OthDirectExpenses', 'OpeningInventory_IndirectWages', 'OpeningInventory_FactoryRentAndRates', 
         'OpeningInventory_FactoryInsurance', 'OpeningInventory_FactoryFuelAndPower', 'OpeningInventory_FactoryGeneralExpenses',
         'OpeningInventory_DeprctnOfFactoryMachinery', 'OpeningInventory_TotalFactoryOverheads', 'OpeningInventory_TotalDebtsManfctrngAcc',
         'ClosingStock_ClsngStckRawMaterial', 'ClosingStock_ClsngStckWrkInPrgrs', 'ClosingStock_ClsngStckTotal', 'CostOfGoodsPrdcd']

        ManufacturingAccount={key:0 for key in ManufacturingAccount_var}
        ManufacturingAccount['manufacturing_account']="not found"

        itr_dict.update(ManufacturingAccount)
    ####trading account

    # trading_keys=t['ITR'][itr_form_type]['TradingAccount'].keys()
    # if 'OtherDirectExpenses' in trading_keys:
    #     nature_list = []
    #     amount_list = []
    #     expense_count = len(t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses'])
    #     for i in range(expense_count):
    #         nature = t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses'][i]['NatureOfDirectExpense']
    #         amount = t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses'][i]['Amount']
    #         nature_list.append(nature)
    #         amount_list.append(amount)
    #     itr_dict['OtherDirectExpenses'] = {'NatureOfDirectExpense':nature_list, 'Amount':amount_list}
    # del t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses']


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    trading_keys=t['ITR'][itr_form_type]['TradingAccount'].keys()
    if 'OtherDirectExpenses' in trading_keys:

        OtherDirectExpenses=pd.DataFrame(t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses'])

        itr_dict['other_direct_expense']=OtherDirectExpenses

        del t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses']
    else:
        itr_dict['other_direct_expense']=np.nan
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
    if 'OtherOperatingRevenueDtls' in trading_keys:
        OtherOperatingRevenueDtls=pd.DataFrame(t['ITR'][itr_form_type]['TradingAccount']['OtherOperatingRevenueDtls'])

        itr_dict['other_revenue_details']=OtherOperatingRevenueDtls
        

        del t['ITR'][itr_form_type]['TradingAccount']['OtherOperatingRevenueDtls']
    else:
        itr_dict['other_revenue_details ']=np.nan
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
    
        
    if 'OtherIncDtls' in trading_keys:

        trading_OtherIncDtls=pd.DataFrame(t['ITR'][itr_form_type]['TradingAccount']['OtherIncDtls'])

        itr_dict['trading_OtherIncDtls']=trading_OtherIncDtls

        del t['ITR'][itr_form_type]['TradingAccount']['OtherIncDtls']

    else:
        itr_dict['trading_OtherIncDtls']=np.nan
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

    trading_account=flatten_json(t['ITR'][itr_form_type]['TradingAccount'])
    itr_dict.update(trading_account)

    ###
    try:
        del t['ITR'][itr_form_type]['PARTA_PL'][ 'DebitsToPL']['OtherExpensesDtls']
    except:
        pass
    try:
        del t['ITR'][itr_form_type]['PARTA_PL']['CreditsToPL']['OthIncome']['OtherIncDtls']
    except:
        pass
    #################################################################################################################   
    # if 'DebitsToPL' in t['ITR'][itr_form_type]['PARTA_PL'] and 'DebitPlAcnt' in t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL'] and 'OtherExpensesDtls' in t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']:
    #     expense_nature_list = []
    #     expense_amount_list = []
    #     expense_count = len(t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'])
    #     for i in range(expense_count):
    #         expense_nature = t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'][i]['ExpenseNature']
    #         expense_amount = t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'][i]['Amount']
    #         expense_nature_list.append(expense_nature)
    #         expense_amount_list.append(expense_amount)
    #     itr_dict['DebitsToPL_DebitPlAcnt_OtherExpensesDtls'] = {'ExpenseNature':expense_nature_list, 'Amount':expense_amount_list}
    # del t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls']

    debit_pla_cnt_keys=t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt'].keys()
    if 'OtherExpensesDtls' in debit_pla_cnt_keys:

        OtherExpensesDtls=pd.DataFrame(t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'])

        itr_dict['other_expense_dtls']=OtherExpensesDtls

        del t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls']
    else:
        itr_dict['other_expense_dtls']=np.nan


    
    PARTA_PL = flatten_json(t['ITR'][itr_form_type]['PARTA_PL'])
    itr_dict.update(PARTA_PL)

    
    
    return itr_dict





