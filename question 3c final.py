import MarkovModelClasses as MarModelCls
# updated paramaters in InputData and Parameter Classes to represent 2000 patients, over 50 years with transition probabilities

MyCohort = MarModelCls.Cohort(id=0, therapy= MONO)
MyCohort.simulate()

MyModel = MarModelCls.CohortOutputs(MyCohort)

print ("Expected life years of a patient in well state at beginning of simulation period",MyModel.get_survival_times())

print("95% confidence interval of survival times", MyModel.get_sumStat_survival_times())
