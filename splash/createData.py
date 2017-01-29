from datetime import datetime

from models import ValaEntryStatus
from models import ValaEntryExperimentType
from models import ValaEntry

veStatus0 = ValaEntryStatus(code="0", string="New")
veStatus1 = ValaEntryStatus(code="1", string="Pending Review")
veStatus2 = ValaEntryStatus(code="2", string="Compleded")
veStatus3 = ValaEntryStatus(code="3", string="Deleted")

veEntry0 = ValaEntryExperimentType(code="0", string="AST")
veEntry1 = ValaEntryExperimentType(code="1", string="Microcentrifuge Disso")
veEntry2 = ValaEntryExperimentType(code="2", string="Thermal Characterization (DSC)")
veEntry3 = ValaEntryExperimentType(code="3", string="Potency")
veEntry4 = ValaEntryExperimentType(code="4", string="Equilibrium Solubility")
veEntry5 = ValaEntryExperimentType(code="5", string="PXRD")
veEntry6 = ValaEntryExperimentType(code="6", string="NMR Characterization")

veEntry0.save()
veEntry1.save()
veEntry2.save()
veEntry3.save()
veEntry4.save()
veEntry5.save()
veEntry6.save()

veStatus0.save()
veStatus1.save()
veStatus2.save()
veStatus3.save()


ve1 = ValaEntry(
    hypothesis = "This is the first hypothesis",
    experimentType = ValaEntryExperimentType.objects.get(code=0),
    status = ValaEntryStatus.objects.get(code=0),
    creationDate = datetime.now(),
    projectID = "AA-012345",
    reviewer = "Head Scientist B"
)

ve2 = ValaEntry(
    hypothesis = "This is the second hypothesis",
    experimentType = ValaEntryExperimentType.objects.get(code=4),
    status = ValaEntryStatus.objects.get(code=1),
    creationDate = datetime.now(),
    projectID = "BB-012345",
    reviewer = "Head Scientist K"
)

ve3 = ValaEntry(
    hypothesis = "This is the second hypothesis",
    experimentType = ValaEntryExperimentType.objects.get(code=2),
    status = ValaEntryStatus.objects.get(code=2),
    creationDate = datetime.now(),
    projectID = "CC-012345",
    reviewer = "Head Scientist K"
)

ve1.save()
ve2.save()
ve3.save()
