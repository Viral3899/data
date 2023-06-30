# import numpy as np
# import pandas as pd
# import json

# def flatten_json(nested_json):
#     out = {}
    
#     def flatten(x, name='', parent_key=''):
#         if type(x) is dict:
#             for a in x:
#                 flatten(x[a], name + a + '_', parent_key=name)
#         elif type(x) is list:
#             if len(x) > 0 and type(x[0]) is dict:
#                 for i, a in enumerate(x):
#                     flatten(a, name, parent_key=name+str(i)+'_')
#             else:
#                 out[parent_key[:-1]] = x
#         else:
#             out[name[:-1]] = x
    
#     flatten(nested_json)
#     return out


# def itr5_json_variable_extraction(t: dict):
#     itr_dict = {}
#     itr_form_type = 'ITR5'
#     itr_form = 'Form_ITR5'
#     itr_keys = t['ITR'][itr_form_type].keys()

#     # Extracted PartA_GEN
#     itr_dict['itr_form'] = t['ITR'][itr_form_type][itr_form]['FormName']
#     itr_dict['assessmentyear'] = t['ITR'][itr_form_type][itr_form]['AssessmentYear']

#     # General itr information
#     itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN1']))

#     # Extracted PartA_GEN2
#     try:
#         nat_bus = flatten_json(t['ITR'][itr_form_type]['PartA_GEN2']['NatOfBus']['NatureOfBusiness'][0])
#         itr_dict.update(nat_bus)
#     except:
#         NatureOfBusiness_var = ['Code', 'TradeName1', 'Description']
#         nat_bus = {key: None for key in NatureOfBusiness_var}
#         itr_dict.update(nat_bus)

#     # 'PARTA_BS'
#     for key in t['ITR'][itr_form_type]['PARTA_BS'].keys():
#         itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PARTA_BS'][key]))

#     # ManufacturingAccount
#     if 'ManufacturingAccount' in itr_keys:
#         ManufacturingAccount = flatten_json(t['ITR'][itr_form_type]['ManufacturingAccount'])
#         ManufacturingAccount['manufacturing_account'] = "found"
#         itr_dict.update(ManufacturingAccount)
#     else:
#         ManufacturingAccount_var = ['OpeningInventory_OpngStckRawMat', 'OpeningInventory_OpngStckWrkinPrgrs',
#                                     'OpeningInventory_OpngInvntryTotal', 'OpeningInventory_Purchases',
#                                     'OpeningInventory_DirectWages', 'OpeningInventory_DirectExpenses',
#                                     'OpeningInventory_CarriageInward', 'OpeningInventory_PowerAndFuel',
#                                     'OpeningInventory_OthDirectExpenses', 'OpeningInventory_IndirectWages',
#                                     'OpeningInventory_FactoryRentAndRates', 'OpeningInventory_FactoryInsurance',
#                                     'OpeningInventory_FactoryFuelAndPower', 'OpeningInventory_FactoryGeneralExpenses',
#                                     'OpeningInventory_DeprctnOfFactoryMachinery', 'OpeningInventory_TotalFactoryOverheads',
#                                     'OpeningInventory_TotalDebtsManfctrngAcc', 'ClosingStock_ClsngStckRawMaterial',
#                                     'ClosingStock_ClsngStckWrkInPrgrs', 'ClosingStock_ClsngStckTotal', 'CostOfGoodsPrdcd']
#         ManufacturingAccount = {key: 0 for key in ManufacturingAccount_var}
#         ManufacturingAccount['manufacturing_account'] = "not found"
#         itr_dict.update(ManufacturingAccount)

#     # Trading account
#     trading_keys = t['ITR'][itr_form_type]['TradingAccount'].keys()
#     if 'OtherOperatingRevenueDtls' in trading_keys:
#         del t['ITR'][itr_form_type]['TradingAccount']['OtherOperatingRevenueDtls']
#     if 'OtherIncDtls' in trading_keys:
#         trading_OtherIncDtls = pd.DataFrame(t['ITR'][itr_form_type]['TradingAccount']['OtherIncDtls'])
#         itr_dict[' '] = trading_OtherIncDtls
#         del t['ITR'][itr_form_type]['TradingAccount']['OtherIncDtls']
#     else:
#         itr_dict['trading_OtherIncDtls'] = np.nan
#     trading_account = flatten_json(t['ITR'][itr_form_type]['TradingAccount'])
#     itr_dict.update(trading_account)

#     try:
#         del t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['OtherExpensesDtls']
#     except:
#         pass
#     try:
#         del t['ITR'][itr_form_type]['PARTA_PL']['CreditsToPL']['OthIncome']['OtherIncDtls']
#     except:
#         pass

#     PARTA_PL = flatten_json(t['ITR'][itr_form_type]['PARTA_PL'])
#     itr_dict.update(PARTA_PL)

#     # Normalize 'DebitsToPL_DebitPlAcnt_OtherExpensesDtls' field if present
#     if 'DebitsToPL' in t['ITR'][itr_form_type]['PARTA_PL'] and 'DebitPlAcnt' in t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL'] and 'OtherExpensesDtls' in t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']:
#         expense_nature_list = []
#         expense_amount_list = []
#         expense_count = len(t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'])
#         for i in range(expense_count):
#             expense_nature = t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'][i].values()
#             expense_amount = t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'][i].values()
            
#             expense_nature_list.append(list(expense_nature)[0])
#             expense_amount_list.append(list(expense_nature)[1])
#         itr_dict['DebitsToPL_DebitPlAcnt_OtherExpensesDtls'] = [expense_nature_list, expense_amount_list]

#     return itr_dict
#########################################################################################################################################################################################################################################
#########################################################################################################################################################################################################################################
#########################################################################################################################################################################################################################################

import numpy as np
import pandas as pd
import json
def flatten_json(nested_json):
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
def itr3_json_variable_extraction(t:dict):
    
    itr_dict={}
    itr_form_type='ITR3'
    itr_form='Form_ITR3'
    itr_kyes=t['ITR'][itr_form_type].keys()
    ##important tags itr3
    # itr=['Form_ITR3', 'PartA_GEN1', 'PartA_GEN2', 'PARTA_BS', 'ManufacturingAccount', 'TradingAccount', 'PARTA_PL']

    ###extracted PartA_GEN
    itr_dict['itr_form']=t['ITR'][itr_form_type][itr_form]['FormName']
    itr_dict['assessmentyear']=t['ITR'][itr_form_type][itr_form]['AssessmentYear']

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    ###general itr information
    # try:
    #     CompDirectorPrvYrDtls_keys=t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['CompDirectorPrvYr'].keys()
    #     print(CompDirectorPrvYrDtls_keys)
    #     if 'CompDirectorPrvYrDtls' in CompDirectorPrvYrDtls_keys:

    #         CompDirectorPrvYrDtls=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['CompDirectorPrvYr']['CompDirectorPrvYrDtls'])

    #         itr_dict['comp_dir_prv_dtls']=CompDirectorPrvYrDtls

    #         del t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['CompDirectorPrvYr']['CompDirectorPrvYrDtls']

    #     else:
    #         itr_dict['comp_dir_prv_dtls']=np.nan
    # except:
    #     pass  
    
    
    # try:
    #     HeldUnlistedEqShrPrYrDtls_keys=t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['HeldUnlistedEqShrPrYr'].keys()
    #     # print(CompDirectorPrvYrDtls_keys)
    #     if 'HeldUnlistedEqShrPrYrDtls' in HeldUnlistedEqShrPrYrDtls_keys:

    #         HeldUnlistedEqShrPrYrDtls=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['HeldUnlistedEqShrPrYr']['HeldUnlistedEqShrPrYrDtls'])

    #         itr_dict['held_units_prv_dtls']=HeldUnlistedEqShrPrYrDtls

    #         del t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['HeldUnlistedEqShrPrYr']['HeldUnlistedEqShrPrYrDtls']

    #     else:
    #         itr_dict['held_units_prv_dtls']=np.nan
    # except:
    #     pass
    
    
    # try:
    #     PartnerInFirmDtls_keys=t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['PartnerInFirm'].keys()
    #     # print(CompDirectorPrvYrDtls_keys)
    #     if 'PartnerInFirmDtls' in PartnerInFirmDtls_keys:

    #         PartnerInFirmDtls=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['PartnerInFirm']['PartnerInFirmDtls'])

    #         itr_dict['parternerfirm_prv_dtls']=PartnerInFirmDtls

    #         del t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['PartnerInFirm']['PartnerInFirmDtls']

    #     else:
    #         itr_dict['parternerfirm_prv_dtls']=np.nan
    # except:
    #     pass
    
    try:
        CompDirectorPrvYrDtls_keys=t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['CompDirectorPrvYr'].keys()
        if 'CompDirectorPrvYrDtls' in CompDirectorPrvYrDtls_keys:

            CompDirectorPrvYrDtls=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['CompDirectorPrvYr']['CompDirectorPrvYrDtls'])

            itr_dict['CompDirectorPrvYrDtls']=CompDirectorPrvYrDtls

            del t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['CompDirectorPrvYr']['CompDirectorPrvYrDtls']

        else:
            itr_dict['CompDirectorPrvYrDtls']=np.nan
    except:
        pass  
    
    
    
    try:
        HeldUnlistedEqShrPrYrDtls_keys=t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['HeldUnlistedEqShrPrYr'].keys()
        if 'HeldUnlistedEqShrPrYrDtls' in HeldUnlistedEqShrPrYrDtls_keys:

            HeldUnlistedEqShrPrYrDtls=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['HeldUnlistedEqShrPrYr']['HeldUnlistedEqShrPrYrDtls'])

            itr_dict['CompDirectorPrvYrDtls']=CompDirectorPrvYrDtls

            del t['ITR'][itr_form_type]['PartA_GEN1']['FilingStatus']['HeldUnlistedEqShrPrYr']['HeldUnlistedEqShrPrYrDtls']

        else:
            itr_dict['HeldUnlistedEqShrPrYrDtls']=np.nan
    except:
        pass    
    
    itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN1']))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    ###extracted PartA_GEN2
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
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Audit_info_keys=t['ITR'][itr_form_type]['PartA_GEN2']['AuditInfo'].keys()
    # if 'AuditDetails' in Audit_info_keys:

    #     AuditDetails=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2']['AuditInfo']['AuditDetails'])

    #     itr_dict['audit_details']=AuditDetails

    #     del t['ITR'][itr_form_type]['PartA_GEN2']['AuditInfo']['AuditDetails']

    # else:
    #         itr_dict['audit_details']=np.nan
   
    # Audit_info_keys=t['ITR'][itr_form_type]['PartA_GEN2']['AuditInfo'].keys()
    # if 'AuditReportDetails' in Audit_info_keys:

    #     AuditReportDetails=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2']['AuditInfo']['AuditReportDetails'])
    #     # print(AuditReportDetails)
        
    #     itr_dict['audit_report_details']=AuditReportDetails

    #     del t['ITR'][itr_form_type]['PartA_GEN2']['AuditInfo']['AuditReportDetails']

    # else:
    #     itr_dict['audit_report_details']=np.nan
    
    
    # itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN2']))







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
    try:
        trading_keys=t['ITR'][itr_form_type]['TradingAccount'].keys()
        if 'OtherDirectExpenses' in trading_keys:

            OtherDirectExpenses=pd.DataFrame(t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses'])

            itr_dict['other_direct_expense']=OtherDirectExpenses

            del t['ITR'][itr_form_type]['TradingAccount']['OtherDirectExpenses']
        else:
            itr_dict['other_direct_expense']=np.nan
    except:
        pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
    if 'OtherOperatingRevenueDtls' in trading_keys:

        del t['ITR'][itr_form_type]['TradingAccount']['OtherOperatingRevenueDtls']
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
    try:
        
        if 'OtherIncDtls' in trading_keys:

            trading_OtherIncDtls=pd.DataFrame(t['ITR'][itr_form_type]['TradingAccount']['OtherIncDtls'])

            itr_dict['trading_OtherIncDtls']=trading_OtherIncDtls

            del t['ITR'][itr_form_type]['TradingAccount']['OtherIncDtls']

        else:
            itr_dict['trading_OtherIncDtls']=np.nan
    except:
        pass
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
      
    try:
        debit_pl_acnt_keys=t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt'].keys()
        if 'OtherExpensesDtls' in debit_pl_acnt_keys:

            OtherExpensesDtls=pd.DataFrame(t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'])

            itr_dict['other_expense_dtls']=OtherExpensesDtls

            del t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls']
        else:
            itr_dict['other_expense_dtls']=np.nan
    except:
        pass

    
    PARTA_PL = flatten_json(t['ITR'][itr_form_type]['PARTA_PL'])
    itr_dict.update(PARTA_PL)

    
    
    return itr_dict





