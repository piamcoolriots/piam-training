from DAOs.TadaBase.TadaBaseUsersDao import TadaBaseUsersDao
from DAOs.Redis.RedisTadaBase.RedisUsersDao import RedisTadaBaseUsersDao
from DAOs.TadaBase.TadaBaseTraineeDao import TadaBaseTraineeDao
from DAOs.Redis.RedisTadaBase.RedisTraineeDao import RedisTadaBaseTraineeDao
from DAOs.TadaBase.TadaBaseRegistrationEnrolmentGrantDao import TadaBaseRegistrationEnrolmentGrantDao
from DAOs.Redis.RedisTadaBase.RedisRegistrationEnrolmentGrantDao import RedisTadaBaseRegistrationEnrolmentGrantDao
from DAOs.TadaBase.TadaBaseCourseDao import TadaBaseCourseDao
from DAOs.Redis.RedisTadaBase.RedisCourseDao import RedisTadaBaseCourseDao
from DAOs.TadaBase.TadaBaseEmployerDao import TadaBaseEmployerDao
from DAOs.Redis.RedisTadaBase.RedisEmployerDao import RedisTadaBaseEmployerDao
from DAOs.TadaBase.TadaBaseMiscellaneousInvoiceItemsDao import TadaBaseMiscellaneousInvoiceItemsDao
from DAOs.Redis.RedisTadaBase.RedisMiscellaneousInvoiceItemsDao import RedisTadaBaseMiscellaneousInvoiceItemsDao
from DAOs.TadaBase.TadaBaseMiscellaneousCreditNoteDao import TadaBaseMiscellaneousCreditNoteDao
from DAOs.Redis.RedisTadaBase.RedisMiscellaneousCreditNoteDao import RedisTadaBaseMiscellaneousCreditNoteDao
from DAOs.TadaBase.TadaBaseMiscellaneousCreditNoteLineDao import TadaBaseMiscellaneousCreditNoteLineDao
from DAOs.Redis.RedisTadaBase.RedisMiscellaneousCreditNoteLineDao import RedisTadaBaseMiscellaneousCreditNoteLineDao
from DAOs.TadaBase.TadaBaseTrainingAndAssessmentProviderDao import TadaBaseTrainingAndAssessmentProviderDao
from DAOs.Redis.RedisTadaBase.RedisTrainingAndAssessmentProviderDao import RedisTadaBaseTrainingAndAssessmentProviderDao
from DAOs.TadaBase.TadaBaseConferringInstituteDao import TadaBaseConferringInstituteDao
from DAOs.Redis.RedisTadaBase.RedisConferringInstituteDao import RedisTadaBaseConferringInstituteDao
# from DAOs.TadaBase.TadaBaseSSICLutDao import TadaBaseSSICLutDao
# from DAOs.Redis.RedisTadaBase.RedisSSICLutDao import RedisTadaBaseSSICLutDao
# from DAOs.TadaBase.TadaBaseNotificationDao import TadaBaseNotificationDao
# from DAOs.Redis.RedisTadaBase.RedisNotificationDao import RedisTadaBaseNotificationDao
from DAOs.TadaBase.TadaBaseCourseSupportDao import TadaBaseCourseSupportDao
from DAOs.Redis.RedisTadaBase.RedisCourseSupportDao import RedisTadaBaseCourseSupportDao
# from DAOs.TadaBase.TadaBaseAreaOfTrainingLutDao import TadaBaseAreaOfTrainingLutDao
# from DAOs.Redis.RedisTadaBase.RedisAreaOfTrainingLutDao import RedisTadaBaseAreaOfTrainingLutDao
from DAOs.TadaBase.TadaBaseTPContactPersonsDao import TadaBaseTPContactPersonsDao
from DAOs.Redis.RedisTadaBase.RedisTPContactPersonsDao import RedisTadaBaseTPContactPersonsDao
from DAOs.TadaBase.TadaBaseTrainerDao import TadaBaseTrainerDao
from DAOs.Redis.RedisTadaBase.RedisTrainerDao import RedisTadaBaseTrainerDao
from DAOs.TadaBase.TadaBaseJobRolesLutDao import TadaBaseJobRolesLutDao
from DAOs.Redis.RedisTadaBase.RedisJobRolesLutDao import RedisTadaBaseJobRolesLutDao
from DAOs.TadaBase.TadaBaseSectorsLutDao import TadaBaseSectorsLutDao
from DAOs.Redis.RedisTadaBase.RedisSectorsLutDao import RedisTadaBaseSectorsLutDao
# from DAOs.TadaBase.TadaBaseJobLevelsLutDao import TadaBaseJobLevelsLutDao
# from DAOs.Redis.RedisTadaBase.RedisJobLevelsLutDao import RedisTadaBaseJobLevelsLutDao
# from DAOs.TadaBase.TadaBaseWSQFrameworksLutDao import TadaBaseWSQFrameworksLutDao
# from DAOs.Redis.RedisTadaBase.RedisWSQFrameworksLutDao import RedisTadaBaseWSQFrameworksLutDao
# from DAOs.TadaBase.TadaBaseEduOfTargetAudsLutDao import TadaBaseEduOfTargetAudsLutDao
# from DAOs.Redis.RedisTadaBase.RedisEduOfTargetAudsLutDao import RedisTadaBaseEduOfTargetAudsLutDao
# from DAOs.TadaBase.TadaBaseFieldOfStudiesLutDao import TadaBaseFieldOfStudiesLutDao
# from DAOs.Redis.RedisTadaBase.RedisFieldOfStudiesLutDao import RedisTadaBaseFieldOfStudiesLutDao
# from DAOs.TadaBase.TadaBaseOccupationsLutDao import TadaBaseOccupationsLutDao
# from DAOs.Redis.RedisTadaBase.RedisOccupationsLutDao import RedisTadaBaseOccupationsLutDao
# from DAOs.TadaBase.TadaBaseSubSectorsLutDao import TadaBaseSubSectorsLutDao
# from DAOs.Redis.RedisTadaBase.RedisSubSectorsLutDao import RedisTadaBaseSubSectorsLutDao
from DAOs.TadaBase.TadaBaseSkillsFrameworksLutDao import TadaBaseSkillsFrameworksLutDao
from DAOs.Redis.RedisTadaBase.RedisSkillsFrameworksLutDao import RedisTadaBaseSkillsFrameworksLutDao
# from DAOs.TadaBase.TadaBaseKeyTaskLutDao import TadaBaseKeyTaskLutDao
# from DAOs.Redis.RedisTadaBase.RedisKeyTaskLutDao import RedisTadaBaseKeyTaskLutDao
# from DAOs.TadaBase.TadaBaseMappedSkillsCompetencyLutDao import TadaBaseMappedSkillsCompetencyLutDao
# from DAOs.Redis.RedisTadaBase.RedisMappedSkillsCompetencyLutDao import RedisTadaBaseMappedSkillsCompetencyLutDao
from DAOs.TadaBase.TadaBaseAddressDao import TadaBaseAddressDao
from DAOs.Redis.RedisTadaBase.RedisAddressDao import RedisTadaBaseAddressDao
# from DAOs.TadaBase.TadaBaseOutcomeAreasLutDao import TadaBaseOutcomeAreasLutDao
# from DAOs.Redis.RedisTadaBase.RedisOutcomeAreasLutDao import RedisTadaBaseOutcomeAreasLutDao
# from DAOs.TadaBase.TadaBaseQualityAreasLutDao import TadaBaseQualityAreasLutDao
# from DAOs.Redis.RedisTadaBase.RedisQualityAreasLutDao import RedisTadaBaseQualityAreasLutDao
# from DAOs.TadaBase.TadaBaseQualificationsLutDao import TadaBaseQualificationsLutDao
# from DAOs.Redis.RedisTadaBase.RedisQualificationsLutDao import RedisTadaBaseQualificationsLutDao
from DAOs.TadaBase.TadaBaseCourseEnquiryDao import TadaBaseCourseEnquiryDao
from DAOs.Redis.RedisTadaBase.RedisCourseEnquiryDao import RedisTadaBaseCourseEnquiryDao
from DAOs.TadaBase.TadaBaseMarketingInfoAndBrochureDao import TadaBaseMarketingInfoAndBrochureDao
from DAOs.Redis.RedisTadaBase.RedisMarketingInfoAndBrochureDao import RedisTadaBaseMarketingInfoAndBrochureDao
from DAOs.TadaBase.TadaBaseCourseSessionTemplateDao import TadaBaseCourseSessionTemplateDao
from DAOs.Redis.RedisTadaBase.RedisCourseSessionTemplateDao import RedisTadaBaseCourseSessionTemplateDao
from DAOs.TadaBase.TadaBaseActivityLogDao import TadaBaseActivityLogDao
from DAOs.Redis.RedisTadaBase.RedisActivityLogDao import RedisTadaBaseActivityLogDao
# from DAOs.TadaBase.TadaBaseTSCCodeLutDao import TadaBaseTSCCodeLutDao
# from DAOs.Redis.RedisTadaBase.RedisTSCCodeLutDao import RedisTadaBaseTSCCodeLutDao
# from DAOs.TadaBase.TadaBaseGSCCodeLutDao import TadaBaseGSCCodeLutDao
# from DAOs.Redis.RedisTadaBase.RedisGSCCodeLutDao import RedisTadaBaseGSCCodeLutDao
from DAOs.TadaBase.TadaBasePaymentDetailsDao import TadaBasePaymentDetailsDao
from DAOs.Redis.RedisTadaBase.RedisPaymentDetailsDao import RedisTadaBasePaymentDetailsDao
from DAOs.TadaBase.TadaBaseBookingBillingAdviceInvoiceDao import TadaBaseBookingBillingAdviceInvoiceDao
from DAOs.Redis.RedisTadaBase.RedisBookingBillingAdviceInvoiceDao import RedisTadaBaseBookingBillingAdviceInvoiceDao
from DAOs.TadaBase.TadaBaseParametersLookupDao import TadaBaseParametersLookupDao
from DAOs.Redis.RedisTadaBase.RedisParametersLookupDao import RedisTadaBaseParametersLookupDao
from DAOs.TadaBase.TadaBaseDiscountLookupDao import TadaBaseDiscountLookupDao
from DAOs.Redis.RedisTadaBase.RedisDiscountLookupDao import RedisTadaBaseDiscountLookupDao
from DAOs.TadaBase.TadaBaseMiscellaneousInvoiceDao import TadaBaseMiscellaneousInvoiceDao
from DAOs.Redis.RedisTadaBase.RedisMiscellaneousInvoiceDao import RedisTadaBaseMiscellaneousInvoiceDao
# from DAOs.TadaBase.TadaBaseUserStoryPagesDao import TadaBaseUserStoryPagesDao
# from DAOs.Redis.RedisTadaBase.RedisUserStoryPagesDao import RedisTadaBaseUserStoryPagesDao
from DAOs.TadaBase.TadaBaseCourseSessionDao import TadaBaseCourseSessionDao
from DAOs.Redis.RedisTadaBase.RedisCourseSessionDao import RedisTadaBaseCourseSessionDao
from DAOs.TadaBase.TadaBaseCourseRunDao import TadaBaseCourseRunDao
from DAOs.Redis.RedisTadaBase.RedisCourseRunDao import RedisTadaBaseCourseRunDao
# from DAOs.TadaBase.TadaBaseContactNumberDao import TadaBaseContactNumberDao
# from DAOs.Redis.RedisTadaBase.RedisContactNumberDao import RedisTadaBaseContactNumberDao
# from DAOs.TadaBase.TadaBaseNotificationsDao import TadaBaseNotificationsDao
# from DAOs.Redis.RedisTadaBase.RedisNotificationsDao import RedisTadaBaseNotificationsDao
# from DAOs.TadaBase.TadaBaseDisplayedNotificationDao import TadaBaseDisplayedNotificationDao
# from DAOs.Redis.RedisTadaBase.RedisDisplayedNotificationDao import RedisTadaBaseDisplayedNotificationDao
# from DAOs.TadaBase.TadaBasePersonasDao import TadaBasePersonasDao
# from DAOs.Redis.RedisTadaBase.RedisPersonasDao import RedisTadaBasePersonasDao
# from DAOs.TadaBase.TadaBaseTestTitlesDao import TadaBaseTestTitlesDao
# from DAOs.Redis.RedisTadaBase.RedisTestTitlesDao import RedisTadaBaseTestTitlesDao
from DAOs.TadaBase.TadaBaseCourseRunTemplateDao import TadaBaseCourseRunTemplateDao
from DAOs.Redis.RedisTadaBase.RedisCourseRunTemplateDao import RedisTadaBaseCourseRunTemplateDao
# from DAOs.TadaBase.TadaBaseClassRequestDao import TadaBaseClassRequestDao
# from DAOs.Redis.RedisTadaBase.RedisClassRequestDao import RedisTadaBaseClassRequestDao
from DAOs.TadaBase.TadaBaseAgentDao import TadaBaseAgentDao
from DAOs.Redis.RedisTadaBase.RedisAgentDao import RedisTadaBaseAgentDao
from DAOs.TadaBase.TadaBaseRefundDetailsDao import TadaBaseRefundDetailsDao
from DAOs.Redis.RedisTadaBase.RedisRefundDetailsDao import RedisTadaBaseRefundDetailsDao
from DAOs.TadaBase.TadaBaseCreditNoteDao import TadaBaseCreditNoteDao
from DAOs.Redis.RedisTadaBase.RedisCreditNoteDao import RedisTadaBaseCreditNoteDao
from DAOs.TadaBase.TadaBaseCreditNoteLineDao import TadaBaseCreditNoteLineDao
from DAOs.Redis.RedisTadaBase.RedisCreditNoteLineDao import RedisTadaBaseCreditNoteLineDao
from DAOs.TadaBase.TadaBaseAttendanceAndAssessmentDao import TadaBaseAttendanceAndAssessmentDao
from DAOs.Redis.RedisTadaBase.RedisAttendanceAndAssessmentDao import RedisTadaBaseAttendanceAndAssessmentDao
from DAOs.TadaBase.TadaBaseSupportingDocumentsDao import TadaBaseSupportingDocumentsDao
from DAOs.Redis.RedisTadaBase.RedisSupportingDocumentsDao import RedisTadaBaseSupportingDocumentsDao
from DAOs.TadaBase.TadaBaseTPBranchDao import TadaBaseTPBranchDao
from DAOs.Redis.RedisTadaBase.RedisTPBranchDao import RedisTadaBaseTPBranchDao
from DAOs.TadaBase.TadaBaseEmployerBranchDao import TadaBaseEmployerBranchDao
from DAOs.Redis.RedisTadaBase.RedisEmployerBranchDao import RedisTadaBaseEmployerBranchDao
from DAOs.TadaBase.TadaBaseEmployerContactPersonsDao import TadaBaseEmployerContactPersonsDao
from DAOs.Redis.RedisTadaBase.RedisEmployerContactPersonsDao import RedisTadaBaseEmployerContactPersonsDao
# from DAOs.TadaBase.TadaBaseBrandDao import TadaBaseBrandDao
# from DAOs.Redis.RedisTadaBase.RedisBrandDao import RedisTadaBaseBrandDao
from DAOs.TadaBase.TadaBaseProgramDao import TadaBaseProgramDao
from DAOs.Redis.RedisTadaBase.RedisProgramDao import RedisTadaBaseProgramDao
from DAOs.TadaBase.TadaBaseProgramRegistrationEnrolmentDao import TadaBaseProgramRegistrationEnrolmentDao
from DAOs.Redis.RedisTadaBase.RedisProgramRegistrationEnrolmentDao import RedisTadaBaseProgramRegistrationEnrolmentDao
from DAOs.TadaBase.TadaBaseProgramCompletionDao import TadaBaseProgramCompletionDao
from DAOs.Redis.RedisTadaBase.RedisProgramCompletionDao import RedisTadaBaseProgramCompletionDao
# from DAOs.TadaBase.TadaBaseChartOfAccountsLutDao import TadaBaseChartOfAccountsLutDao
# from DAOs.Redis.RedisTadaBase.RedisChartOfAccountsLutDao import RedisTadaBaseChartOfAccountsLutDao
from DAOs.TadaBase.TadaBasePaymentBreakdownDao import TadaBasePaymentBreakdownDao
from DAOs.Redis.RedisTadaBase.RedisPaymentBreakdownDao import RedisTadaBasePaymentBreakdownDao
# from DAOs.TadaBase.TadaBaseCorporateHrDao import TadaBaseCorporateHrDao
# from DAOs.Redis.RedisTadaBase.RedisCorporateHrDao import RedisTadaBaseCorporateHrDao
from DAOs.TadaBase.TadaBaseAgencyDao import TadaBaseAgencyDao
from DAOs.Redis.RedisTadaBase.RedisAgencyDao import RedisTadaBaseAgencyDao
from DAOs.TadaBase.TadaBaseVenueWithStreetAndBuildingDao import TadaBaseVenueWithStreetAndBuildingDao
from DAOs.Redis.RedisTadaBase.RedisVenueWithStreetAndBuildingDao import RedisTadaBaseVenueWithStreetAndBuildingDao
from DAOs.TadaBase.TadaBaseVenueWithRoomDao import TadaBaseVenueWithRoomDao
from DAOs.Redis.RedisTadaBase.RedisVenueWithRoomDao import RedisTadaBaseVenueWithRoomDao
from DAOs.TadaBase.TadaBaseVenueWithFloorAndUnitDao import TadaBaseVenueWithFloorAndUnitDao
from DAOs.Redis.RedisTadaBase.RedisVenueWithFloorAndUnitDao import RedisTadaBaseVenueWithFloorAndUnitDao
from DAOs.TadaBase.TadaBaseSkillsCodeLutDao import TadaBaseSkillsCodeLutDao
from DAOs.Redis.RedisTadaBase.RedisSkillsCodeLutDao import RedisTadaBaseSkillsCodeLutDao
# from DAOs.TadaBase.TadaBaseRoleLookupTableDao import TadaBaseRoleLookupTableDao
# from DAOs.Redis.RedisTadaBase.RedisRoleLookupTableDao import RedisTadaBaseRoleLookupTableDao
# from DAOs.TadaBase.TadaBaseFrameworkLutDao import TadaBaseFrameworkLutDao
# from DAOs.Redis.RedisTadaBase.RedisFrameworkLutDao import RedisTadaBaseFrameworkLutDao
from DAOs.TadaBase.TadaBaseRefundRequestDao import TadaBaseRefundRequestDao
from DAOs.Redis.RedisTadaBase.RedisRefundRequestDao import RedisTadaBaseRefundRequestDao
from DAOs.TadaBase.TadaBaseTPStaffDao import TadaBaseTPStaffDao
from DAOs.Redis.RedisTadaBase.RedisTPStaffDao import RedisTadaBaseTPStaffDao
from DAOs.TadaBase.TadaBaseTrainerFeesLookupDao import TadaBaseTrainerFeesLookupDao
from DAOs.Redis.RedisTadaBase.RedisTrainerFeesLookupDao import RedisTadaBaseTrainerFeesLookupDao
from DAOs.TadaBase.TadaBaseVenueAvailabilityDao import TadaBaseVenueAvailabilityDao
from DAOs.Redis.RedisTadaBase.RedisVenueAvailabilityDao import RedisTadaBaseVenueAvailabilityDao
from DAOs.TadaBase.TadaBaseTrainerTimesheetDao import TadaBaseTrainerTimesheetDao
from DAOs.Redis.RedisTadaBase.RedisTrainerTimesheetDao import RedisTadaBaseTrainerTimesheetDao
# from DAOs.TadaBase.TadaBaseServicesDao import TadaBaseServicesDao
# from DAOs.Redis.RedisTadaBase.RedisServicesDao import RedisTadaBaseServicesDao
from DAOs.TadaBase.TadaBaseAgentCommisionLookupDao import TadaBaseAgentCommisionLookupDao
from DAOs.Redis.RedisTadaBase.RedisAgentCommisionLookupDao import RedisTadaBaseAgentCommisionLookupDao
from DAOs.TadaBase.TadaBaseTrainerAssignmentDao import TadaBaseTrainerAssignmentDao
from DAOs.Redis.RedisTadaBase.RedisTrainerAssignmentDao import RedisTadaBaseTrainerAssignmentDao
# from DAOs.TadaBase.TadaBaseAPILoginCredentialsDao import TadaBaseAPILoginCredentialsDao
# from DAOs.Redis.RedisTadaBase.RedisAPILoginCredentialsDao import RedisTadaBaseAPILoginCredentialsDao
# from DAOs.TadaBase.TadaBaseRunningNumberDao import TadaBaseRunningNumberDao
# from DAOs.Redis.RedisTadaBase.RedisRunningNumberDao import RedisTadaBaseRunningNumberDao
from DAOs.TadaBase.TadaBaseAgentSalesDao import TadaBaseAgentSalesDao
from DAOs.Redis.RedisTadaBase.RedisAgentSalesDao import RedisTadaBaseAgentSalesDao
from DAOs.TadaBase.TadaBaseTrainerAvailabilityDao import TadaBaseTrainerAvailabilityDao
from DAOs.Redis.RedisTadaBase.RedisTrainerAvailabilityDao import RedisTadaBaseTrainerAvailabilityDao
from DAOs.TadaBase.TadaBaseCreditNoteReasonsDao import TadaBaseCreditNoteReasonsDao
from DAOs.Redis.RedisTadaBase.RedisCreditNoteReasonsDao import RedisTadaBaseCreditNoteReasonsDao
# from DAOs.TadaBase.TadaBaseBankAccountLutDao import TadaBaseBankAccountLutDao
# from DAOs.Redis.RedisTadaBase.RedisBankAccountLutDao import RedisTadaBaseBankAccountLutDao
from DAOs.TadaBase.TadaBaseAgentCommissionCategoryDao import TadaBaseAgentCommissionCategoryDao
from DAOs.Redis.RedisTadaBase.RedisAgentCommissionCategoryDao import RedisTadaBaseAgentCommissionCategoryDao
from DAOs.TadaBase.TadaBaseTrainerFeesCategoryDao import TadaBaseTrainerFeesCategoryDao
from DAOs.Redis.RedisTadaBase.RedisTrainerFeesCategoryDao import RedisTadaBaseTrainerFeesCategoryDao
# from DAOs.TadaBase.TadaBaseBCVenueCodeDao import TadaBaseBCVenueCodeDao
# from DAOs.Redis.RedisTadaBase.RedisBCVenueCodeDao import RedisTadaBaseBCVenueCodeDao
from DAOs.TadaBase.TadaBaseUserStoryPagesTraineeDao import TadaBaseUserStoryPagesTraineeDao
from DAOs.Redis.RedisTadaBase.RedisUserStoryPagesTraineeDao import RedisTadaBaseUserStoryPagesTraineeDao
# from DAOs.TadaBase.TadaBaseStripePaymentsDao import TadaBaseStripePaymentsDao
# from DAOs.Redis.RedisTadaBase.RedisStripePaymentsDao import RedisTadaBaseStripePaymentsDao
# from DAOs.TadaBase.TadaBaseCourseEnquiryFormDao import TadaBaseCourseEnquiryFormDao
# from DAOs.Redis.RedisTadaBase.RedisCourseEnquiryFormDao import RedisTadaBaseCourseEnquiryFormDao
# from DAOs.TadaBase.TadaBaseBookingTemporaryTableDao import TadaBaseBookingTemporaryTableDao
# from DAOs.Redis.RedisTadaBase.RedisBookingTemporaryTableDao import RedisTadaBaseBookingTemporaryTableDao
#
#
records = TadaBaseUsersDao().retrieve()
print("users records: ", len(records.users))
RedisTadaBaseUsersDao().insert(records)
#
records = TadaBaseTraineeDao().retrieve()
print("trainee records: ", len(records.trainee))
RedisTadaBaseTraineeDao().insert(records)
# #
records = TadaBaseRegistrationEnrolmentGrantDao().retrieve()
print("registrationEnrolmentGrant records: ", len(records.registrationEnrolmentGrant))
RedisTadaBaseRegistrationEnrolmentGrantDao().insert(records)
# #
records = TadaBaseCourseDao().retrieve()
print("course records: ", len(records.course))
RedisTadaBaseCourseDao().insert(records)
#
records = TadaBaseEmployerDao().retrieve()
print("employer records: ", len(records.employer))
RedisTadaBaseEmployerDao().insert(records)

records = TadaBaseTrainingAndAssessmentProviderDao().retrieve()
print("trainingAndAssessmentProvider records: ", len(records.trainingAndAssessmentProvider))
RedisTadaBaseTrainingAndAssessmentProviderDao().insert(records)

# records = TadaBaseConferringInstituteDao().retrieve()
# print("conferringInstitute records: ", len(records.conferringInstitute))
# RedisTadaBaseConferringInstituteDao().insert(records)
#
# records = TadaBaseSSICLutDao().retrieve()
# print("sSICLut records: ", len(records.sSICLut))
# RedisTadaBaseSSICLutDao().insert(records)
#
# records = TadaBaseNotificationDao().retrieve()
# print("notification records: ", len(records.notification))
# RedisTadaBaseNotificationDao().insert(records)
#
# records = TadaBaseCourseSupportDao().retrieve()
# print("courseSupport records: ", len(records.courseSupport))
# RedisTadaBaseCourseSupportDao().insert(records)
#
# records = TadaBaseAreaOfTrainingLutDao().retrieve()
# print("areaOfTrainingLut records: ", len(records.areaOfTrainingLut))
# RedisTadaBaseAreaOfTrainingLutDao().insert(records)
#
records = TadaBaseTPContactPersonsDao().retrieve()
print("tPContactPersons records: ", len(records.tPContactPersons))
RedisTadaBaseTPContactPersonsDao().insert(records)
#VenuewithStreetandBuildingDao
records = TadaBaseVenuewithStreetandBuildingDao().retrieve()
print("VenuewithStreetandBuilding records: ", len(records.VenuewithStreetandBuilding))
RedisTadaBaseVenuewithStreetandBuildingDao().insert(records)
# 
records = TadaBaseVenuewithFloorandUnitDao().retrieve()
print("VenuewithFloorandUnit records: ", len(records.VenuewithFloorandUnit))
RedisTadaBaseVenuewithFloorandUnitDao().insert(records)
# 
records = TadaBaseVenuewithRoomDao().retrieve()
print("VenuewithRoom records: ", len(records.VenuewithRoom))
RedisTadaBaseVenuewithRoomDao().insert(records)
# 
records = TadaBaseTrainerDao().retrieve()
print("trainer records: ", len(records.trainer))
RedisTadaBaseTrainerDao().insert(records)
#
# records = TadaBaseJobRolesLutDao().retrieve()
# print("jobRolesLut records: ", len(records.jobRolesLut))
# RedisTadaBaseJobRolesLutDao().insert(records)
#
# records = TadaBaseSectorsLutDao().retrieve()
# print("sectorsLut records: ", len(records.sectorsLut))
# RedisTadaBaseSectorsLutDao().insert(records)
#
# records = TadaBaseJobLevelsLutDao().retrieve()
# print("jobLevelsLut records: ", len(records.jobLevelsLut))
# RedisTadaBaseJobLevelsLutDao().insert(records)
#
# records = TadaBaseWSQFrameworksLutDao().retrieve()
# print("wSQFrameworksLut records: ", len(records.wSQFrameworksLut))
# RedisTadaBaseWSQFrameworksLutDao().insert(records)
#
# records = TadaBaseEduOfTargetAudsLutDao().retrieve()
# print("eduOfTargetAudsLut records: ", len(records.eduOfTargetAudsLut))
# RedisTadaBaseEduOfTargetAudsLutDao().insert(records)
#
# records = TadaBaseFieldOfStudiesLutDao().retrieve()
# print("fieldOfStudiesLut records: ", len(records.fieldOfStudiesLut))
# RedisTadaBaseFieldOfStudiesLutDao().insert(records)
#
# records = TadaBaseOccupationsLutDao().retrieve()
# print("occupationsLut records: ", len(records.occupationsLut))
# RedisTadaBaseOccupationsLutDao().insert(records)
#
# records = TadaBaseSubSectorsLutDao().retrieve()
# print("subSectorsLut records: ", len(records.subSectorsLut))
# RedisTadaBaseSubSectorsLutDao().insert(records)
#
# records = TadaBaseSkillsFrameworksLutDao().retrieve()
# print("skillsFrameworksLut records: ", len(records.skillsFrameworksLut))
# RedisTadaBaseSkillsFrameworksLutDao().insert(records)
#
# records = TadaBaseKeyTaskLutDao().retrieve()
# print("keyTaskLut records: ", len(records.keyTaskLut))
# RedisTadaBaseKeyTaskLutDao().insert(records)
#
# records = TadaBaseMappedSkillsCompetencyLutDao().retrieve()
# print("mappedSkillsCompetencyLut records: ", len(records.mappedSkillsCompetencyLut))
# RedisTadaBaseMappedSkillsCompetencyLutDao().insert(records)
#
records = TadaBaseAddressDao().retrieve()
print("address records: ", len(records.address))
RedisTadaBaseAddressDao().insert(records)
#
# records = TadaBaseOutcomeAreasLutDao().retrieve()
# print("outcomeAreasLut records: ", len(records.outcomeAreasLut))
# RedisTadaBaseOutcomeAreasLutDao().insert(records)
#
# records = TadaBaseQualityAreasLutDao().retrieve()
# print("qualityAreasLut records: ", len(records.qualityAreasLut))
# RedisTadaBaseQualityAreasLutDao().insert(records)
#
# records = TadaBaseQualificationsLutDao().retrieve()
# print("qualificationsLut records: ", len(records.qualificationsLut))
# RedisTadaBaseQualificationsLutDao().insert(records)
# #
# records = TadaBaseCourseEnquiryDao().retrieve()
# print("courseEnquiry records: ", len(records.courseEnquiry))
# RedisTadaBaseCourseEnquiryDao().insert(records)
#
records = TadaBaseMarketingInfoAndBrochureDao().retrieve()
print("marketingInfoAndBrochure records: ", len(records.marketingInfoAndBrochure))
RedisTadaBaseMarketingInfoAndBrochureDao().insert(records)
#
# records = TadaBaseCourseSessionTemplateDao().retrieve()
# print("courseSessionTemplate records: ", len(records.courseSessionTemplate))
# RedisTadaBaseCourseSessionTemplateDao().insert(records)
# #
# records = TadaBaseActivityLogDao().retrieve()
# print("activityLog records: ", len(records.activityLog))
# RedisTadaBaseActivityLogDao().insert(records)
#
# records = TadaBaseTSCCodeLutDao().retrieve()
# print("tSCCodeLut records: ", len(records.tSCCodeLut))
# RedisTadaBaseTSCCodeLutDao().insert(records)
#
# records = TadaBaseGSCCodeLutDao().retrieve()
# print("gSCCodeLut records: ", len(records.gSCCodeLut))
# RedisTadaBaseGSCCodeLutDao().insert(records)
# #
records = TadaBasePaymentDetailsDao().retrieve()
print("paymentDetails records: ", len(records.paymentDetails))
RedisTadaBasePaymentDetailsDao().insert(records)
#
records = TadaBaseBookingBillingAdviceInvoiceDao().retrieve()
print("bookingBillingAdviceInvoice records: ", len(records.bookingBillingAdviceInvoice))
RedisTadaBaseBookingBillingAdviceInvoiceDao().insert(records)
#
# records = TadaBaseParametersLookupDao().retrieve()
# print("parametersLookup records: ", len(records.parametersLookup))
# RedisTadaBaseParametersLookupDao().insert(records)
#
# records = TadaBaseDiscountLookupDao().retrieve()
# print("discountLookup records: ", len(records.discountLookup))
# RedisTadaBaseDiscountLookupDao().insert(records)
# #
records = TadaBaseCourseSessionDao().retrieve()
print("courseSession records: ", len(records.courseSession))
RedisTadaBaseCourseSessionDao().insert(records)
#
records = TadaBaseCourseRunDao().retrieve()
print("courseRun records: ", len(records.courseRun))
RedisTadaBaseCourseRunDao().insert(records)

# records = TadaBaseContactNumberDao().retrieve()
# print("contactNumber records: ", len(records.contactNumber))
# RedisTadaBaseContactNumberDao().insert(records)
#
# records = TadaBaseNotificationsDao().retrieve()
# print("notifications records: ", len(records.notifications))
# RedisTadaBaseNotificationsDao().insert(records)
#
# records = TadaBaseDisplayedNotificationDao().retrieve()
# print("displayedNotification records: ", len(records.displayedNotification))
# RedisTadaBaseDisplayedNotificationDao().insert(records)
#
# records = TadaBasePersonasDao().retrieve()
# print("personas records: ", len(records.personas))
# RedisTadaBasePersonasDao().insert(records)
#
# records = TadaBaseCourseRunTemplateDao().retrieve()
# print("courseRunTemplate records: ", len(records.courseRunTemplate))
# RedisTadaBaseCourseRunTemplateDao().insert(records)
# #
# records = TadaBaseClassRequestDao().retrieve()
# print("classRequest records: ", len(records.classRequest))
# RedisTadaBaseClassRequestDao().insert(records)
#
# records = TadaBaseAgentDao().retrieve()
# print("agent records: ", len(records.agent))
# RedisTadaBaseAgentDao().insert(records)
#
records = TadaBaseRefundDetailsDao().retrieve()
print("refundDetails records: ", len(records.refundDetails))
RedisTadaBaseRefundDetailsDao().insert(records)
#
records = TadaBaseCreditNoteDao().retrieve()
print("creditNote records: ", len(records.creditNote))
RedisTadaBaseCreditNoteDao().insert(records)

records = TadaBaseCreditNoteLineDao().retrieve()
print("creditNote records: ", len(records.creditNoteLine))
RedisTadaBaseCreditNoteDao().insert(records)
#
records = TadaBaseAttendanceAndAssessmentDao().retrieve()
print("attendanceAndAssessment records: ", len(records.attendanceAndAssessment))
RedisTadaBaseAttendanceAndAssessmentDao().insert(records)
#
# records = TadaBaseSupportingDocumentsDao().retrieve()
# print("supportingDocuments records: ", len(records.supportingDocuments))
# RedisTadaBaseSupportingDocumentsDao().insert(records)
#
records = TadaBaseTPBranchDao().retrieve()
print("tPBranch records: ", len(records.tPBranch))
RedisTadaBaseTPBranchDao().insert(records)
#
records = TadaBaseEmployerBranchDao().retrieve()
print("employerBranch records: ", len(records.employerBranch))
RedisTadaBaseEmployerBranchDao().insert(records)
#
records = TadaBaseEmployerContactPersonsDao().retrieve()
print("employerContactPersons records: ", len(records.employerContactPersons))
RedisTadaBaseEmployerContactPersonsDao().insert(records)

# records = TadaBaseMiscellaneousCreditNoteDao().retrieve()
# print("Miscellaneous Credit Note records: ", len(records.miscellaneousCreditNote))
# RedisTadaBaseMiscellaneousCreditNoteDao().insert(records)

# records = TadaBaseMiscellaneousCreditNoteLineDao().retrieve()
# print("Miscellaneous Credit Note Line records: ", len(records.miscellaneousCreditNoteLine))
# RedisTadaBaseMiscellaneousCreditNoteLineDao().insert(records)


# records = TadaBaseMiscellaneousInvoiceDao().retrieve()
# print("MiscellaneousInvoice records: ", len(records.miscellaneousInvoice))
# RedisTadaBaseMiscellaneousInvoiceDao().insert(records)

# records = TadaBaseMiscellaneousInvoiceItemsDao().retrieve()
# print("TadaBaseMiscellaneousInvoiceItems records: ", len(records.miscellaneousInvoiceItems))
# RedisTadaBaseMiscellaneousInvoiceItemsDao().insert(records)
# # #
# records = TadaBaseBrandDao().retrieve()
# print("brand records: ", len(records.brand))
# RedisTadaBaseBrandDao().insert(records)
#
# records = TadaBaseProgramDao().retrieve()
# print("program records: ", len(records.program))
# RedisTadaBaseProgramDao().insert(records)
# #
# records = TadaBaseProgramRegistrationEnrolmentDao().retrieve()
# print("programRegistrationEnrolment records: ", len(records.programRegistrationEnrolment))
# RedisTadaBaseProgramRegistrationEnrolmentDao().insert(records)
# #
# records = TadaBaseProgramCompletionDao().retrieve()
# print("programCompletion records: ", len(records.programCompletion))
# RedisTadaBaseProgramCompletionDao().insert(records)
#
# records = TadaBaseChartOfAccountsLutDao().retrieve()
# print("chartOfAccountsLut records: ", len(records.chartOfAccountsLut))
# RedisTadaBaseChartOfAccountsLutDao().insert(records)
#
records = TadaBasePaymentBreakdownDao().retrieve()
print("paymentBreakdown records: ", len(records.paymentBreakdown))
RedisTadaBasePaymentBreakdownDao().insert(records)
#
# records = TadaBaseCorporateHrDao().retrieve()
# print("corporateHr records: ", len(records.corporateHr))
# RedisTadaBaseCorporateHrDao().insert(records)
#
# records = TadaBaseAgencyDao().retrieve()
# print("agency records: ", len(records.agency))
# RedisTadaBaseAgencyDao().insert(records)
# #
# records = TadaBaseVenueWithSa
#
# records = TadaBaseSkillsCodeLutDao().retrieve()
# print("skillsCodeLut records: ", len(records.skillsCodeLut))
# RedisTadaBaseSkillsCodeLutDao().insert(records)
#
# records = TadaBaseRoleLookupTableDao().retrieve()
# print("roleLookupTable records: ", len(records.roleLookupTable))
# RedisTadaBaseRoleLookupTableDao().insert(records)
#
# records = TadaBaseFrameworkLutDao().retrieve()
# print("frameworkLut records: ", len(records.frameworkLut))
# RedisTadaBaseFrameworkLutDao().insert(records)
# #
records = TadaBaseRefundRequestDao().retrieve()
print("refundRequest records: ", len(records.refundRequest))
RedisTadaBaseRefundRequestDao().insert(records)
#
records = TadaBaseTPStaffDao().retrieve()
print("tPStaff records: ", len(records.tPStaff))
RedisTadaBaseTPStaffDao().insert(records)
#
# records = TadaBaseTrainerFeesLookupDao().retrieve()
# print("trainerFeesLookup records: ", len(records.trainerFeesLookup))
# RedisTadaBaseTrainerFeesLookupDao().insert(records)
# #
# records = TadaBaseTrainerTimesheetDao().retrieve()
# print("trainerTimesheet records: ", len(records.trainerTimesheet))
# RedisTadaBaseTrainerTimesheetDao().insert(records)
# #
# records = TadaBaseServicesDao().retrieve()
# print("services records: ", len(records.services))
# RedisTadaBaseServicesDao().insert(records)
#
# records = TadaBaseAgentCommisionLookupDao().retrieve()
# print("agentCommisionLookup records: ", len(records.agentCommisionLookup))
# RedisTadaBaseAgentCommisionLookupDao().insert(records)
# #
# records = TadaBaseTrainerAssignmentDao().retrieve()
# print("trainerAssignment records: ", len(records.trainerAssignment))
# RedisTadaBaseTrainerAssignmentDao().insert(records)
#
# records = TadaBaseAPILoginCredentialsDao().retrieve()
# print("aPILoginCredentials records: ", len(records.aPILoginCredentials))
# RedisTadaBaseAPILoginCredentialsDao().insert(records)
#
# records = TadaBaseRunningNumberDao().retrieve()
# print("runningNumber records: ", len(records.runningNumber))
# RedisTadaBaseRunningNumberDao().insert(records)
# #
# records = TadaBaseAgentSalesDao().retrieve()
# print("agentSales records: ", len(records.agentSales))
# RedisTadaBaseAgentSalesDao().insert(records)
#
#
#
records = TadaBaseCreditNoteReasonsDao().retrieve()
print("creditNoteReasons records: ", len(records.creditNoteReasons))
RedisTadaBaseCreditNoteReasonsDao().insert(records)
#
# records = TadaBaseBankAccountLutDao().retrieve()
# print("bankAccountLut records: ", len(records.bankAccountLut))
# RedisTadaBaseBankAccountLutDao().insert(records)
#
# records = TadaBaseAgentCommissionCategoryDao().retrieve()
# print("agentCommissionCategory records: ", len(records.agentCommissionCategory))
# RedisTadaBaseAgentCommissionCategoryDao().insert(records)
# #
# records = TadaBaseTrainerFeesCategoryDao().retrieve()
# print("trainerFeesCategory records: ", len(records.trainerFeesCategory))
# RedisTadaBaseTrainerFeesCategoryDao().insert(records)
#
# records = TadaBaseBCVenueCodeDao().retrieve()
# print("bCVenueCode records: ", len(records.bCVenueCode))
# RedisTadaBaseBCVenueCodeDao().insert(records)
#
# records = TadaBaseCourseEnquiryFormDao().retrieve()
# print("courseEnquiryForm records: ", len(records.courseEnquiryForm))
# RedisTadaBaseCourseEnquiryFormDao().insert(records)
#
#
#
# need to mirror later
# records = TadaBaseTrainerAvailabilityDao().retrieve()
# print("trainerAvailability records: ", len(records.trainerAvailability))
# RedisTadaBaseTrainerAvailabilityDao().insert(records)
#
# need to mirror later
# records = TadaBaseVenueAvailabilityDao().retrieve()
# print("venueAvailability records: ", len(records.venueAvailability))
# RedisTadaBaseVenueAvailabilityDao().insert(records)
#
#
# not mirrored
#
# records = TadaBaseUserStoryPagesTraineeDao().retrieve()
# print("userStoryPagesTrainee records: ", len(records.userStoryPagesTrainee))
# RedisTadaBaseUserStoryPagesTraineeDao().insert(records)
#
# records = TadaBaseStripePaymentsDao().retrieve()
# print("stripePayments records: ", len(records.stripePayments))
# RedisTadaBaseStripePaymentsDao().insert(records)
#
#
#
# records = TadaBaseBookingTemporaryTableDao().retrieve()
# print("bookingTemporaryTable records: ", len(records.bookingTemporaryTable))
# RedisTadaBaseBookingTemporaryTableDao().insert(records)
#
# no need to mirror
# records = TadaBaseTestTitlesDao().retrieve()
# print("testTitles records: ", len(records.testTitles))
# RedisTadaBaseTestTitlesDao().insert(records)
#
# need to check
#
# no need to mirror
# records = TadaBaseUserStoryPagesDao().retrieve()
# print("userStoryPages records: ", len(records.userStoryPages))
# RedisTadaBaseUserStoryPagesDao().insert(records)