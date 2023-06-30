

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
def itr6_json_variable_extraction(t:dict):
    
    itr_dict={}
    itr_form_type='ITR6'
    itr_form='Form_ITR6'
    itr_kyes=t['ITR'][itr_form_type].keys()
  

    ###extracted PartA_GEN
    itr_dict['itr_form']=t['ITR'][itr_form_type][itr_form]['FormName']
    itr_dict['assessmentyear']=t['ITR'][itr_form_type][itr_form]['AssessmentYear']

    ###general itr infomation
    itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN1']))
    # print(itr_dict)

    ###extracted PartA_GEN2For6
    try:
        PartA_GEN2_keys = t['ITR'][itr_form_type]['PartA_GEN2For6'].keys()
        # print(PartA_GEN2_keys)
        if 'KeyPersons' in PartA_GEN2_keys:
            KeyPersons=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2For6']['KeyPersons'])
            itr_dict['keyperson_info']=KeyPersons

            del t['ITR'][itr_form_type]['PartA_GEN2For6']['KeyPersons']

        else:
            itr_dict['keyperson_info']=np.nan

    except:
        pass
    
    
    try:
        PartA_GEN2_keys = t['ITR'][itr_form_type]['PartA_GEN2For6'].keys()
        # print(PartA_GEN2_keys)
        if 'OwnershipInfo' in PartA_GEN2_keys:
            OwnershipInfo=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2For6']['OwnershipInfo'])
            itr_dict['ownership_info']=OwnershipInfo

            del t['ITR'][itr_form_type]['PartA_GEN2For6']['OwnershipInfo']

        else:
            itr_dict['ownership_info']=np.nan

    except:
        pass
    
    try:
        PartA_GEN2_keys = t['ITR'][itr_form_type]['PartA_GEN2For6'].keys()
        # print(PartA_GEN2_keys)
        if  'ShareHolderInfo' in PartA_GEN2_keys:
            
            ShareHolderInfo=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2For6']['ShareHolderInfo'])

            itr_dict['shareholder_info']=ShareHolderInfo
            del t['ITR'][itr_form_type]['PartA_GEN2For6']['ShareHolderInfo']


        else:
            itr_dict['shareholder_info']=np.nan
    except:
        pass
    
    
    try:
        PartA_GEN2_keys = t['ITR'][itr_form_type]['PartA_GEN2For6'].keys()
        # print(PartA_GEN2_keys)
        if  'AuditReportDetails' in PartA_GEN2_keys:
            
            AuditReportDetails=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2For6']['AuditReportDetails'])

            itr_dict['auditreport_info']=AuditReportDetails
            del t['ITR'][itr_form_type]['PartA_GEN2For6']['AuditReportDetails']


        else:
            itr_dict['auditreport_info']=np.nan
    except:
        pass
    
    nature_of_bus_keys=t['ITR'][itr_form_type]['PartA_GEN2For6']['NatOfBus'].keys()
    if 'NatureOfBusiness' in nature_of_bus_keys:

        NatureOfBusiness=pd.DataFrame(t['ITR'][itr_form_type]['PartA_GEN2For6']['NatOfBus']['NatureOfBusiness'])

        itr_dict['nature_of_business']=NatureOfBusiness

        del t['ITR'][itr_form_type]['PartA_GEN2For6']['NatOfBus']['NatureOfBusiness']

    else:
        itr_dict['nature_of_business']=np.nan
    

    itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN2For6']))

    
    shareholder_funds_keys=t['ITR'][itr_form_type]['PARTA_BSFor6FrmAY13']['EquityAndLiablities'].keys()
    if 'ShareHolderFund' in shareholder_funds_keys:

        ShareHolderFund=pd.DataFrame(t['ITR'][itr_form_type]['PARTA_BSFor6FrmAY13']['EquityAndLiablities']['ShareHolderFund'])

        itr_dict['shareholder_fund']=ShareHolderFund

        del t['ITR'][itr_form_type]['PARTA_BSFor6FrmAY13']['EquityAndLiablities']['ShareHolderFund']

    else:
        itr_dict['shareholder_fund']=np.nan
    

    # itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PartA_GEN2For6']))

    
    
    
    
    ###'PARTA_BS'   
    for key in t['ITR'][itr_form_type]['PARTA_BSFor6FrmAY13'].keys():

        itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PARTA_BSFor6FrmAY13'][key]))
    
    for key in t['ITR'][itr_form_type]['PARTA_BSIndAS'].keys():

        itr_dict.update(flatten_json(t['ITR'][itr_form_type]['PARTA_BSIndAS'][key]))
    

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

    debit_pla_cnt_keys=t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt'].keys()
    if 'OtherExpensesDtls' in debit_pla_cnt_keys:

        OtherExpensesDtls=pd.DataFrame(t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls'])

        itr_dict['other_expense_dtls']=OtherExpensesDtls

        del t['ITR'][itr_form_type]['PARTA_PL']['DebitsToPL']['DebitPlAcnt']['OtherExpensesDtls']
    else:
        itr_dict['other_expense_dtls']=np.nan


    
    parta_pl_keys=t['ITR'][itr_form_type]['PARTA_PL'].keys()
    if 'NoBooksOfAccPLDetails' in parta_pl_keys:

        NoBooksOfAccPLDetails=pd.DataFrame(t['ITR'][itr_form_type]['PARTA_PL']['NoBooksOfAccPLDetails'])

        itr_dict['notebook_details']=NoBooksOfAccPLDetails

        del t['ITR'][itr_form_type]['PARTA_PL']['NoBooksOfAccPLDetails']
    else:
        itr_dict['other_expense_dtls']=np.nan
    
    PARTA_PL = flatten_json(t['ITR'][itr_form_type]['PARTA_PL'])
    itr_dict.update(PARTA_PL)

    
    
    return itr_dict





