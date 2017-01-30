from datetime import datetime
from django.utils import timezone

from splash.models import Status
from splash.models import ExperimentType
from splash.models import ValaEntry

veStatus0 = Status(code="0", text="New")
veStatus1 = Status(code="1", text="Pending Review")
veStatus2 = Status(code="2", text="Compleded")
veStatus3 = Status(code="3", text="Deleted")

veEntry0 = ExperimentType(code="0", name="AST")
veEntry1 = ExperimentType(code="1", name="Microcentrifuge Disso")
veEntry2 = ExperimentType(code="2", name="Thermal Characterization (DSC)")
veEntry3 = ExperimentType(code="3", name="Potency")
veEntry4 = ExperimentType(code="4", name="Equilibrium Solubility")
veEntry5 = ExperimentType(code="5", name="PXRD")
veEntry6 = ExperimentType(code="6", name="NMR Characterization")

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
    experimentType = ExperimentType.objects.get(code=0),
    status = Status.objects.get(code=0),
    creationDate = timezone.now(),
    projectID = "AA-012345",
    reviewer = "Head Scientist B"
)

ve2 = ValaEntry(
    hypothesis = "This is the second hypothesis",
    experimentType = ExperimentType.objects.get(code=4),
    status = Status.objects.get(code=1),
    creationDate = timezone.now(),
    projectID = "BB-012345",
    reviewer = "Head Scientist K"
)

ve3 = ValaEntry(
    hypothesis = "This is the second hypothesis",
    experimentType = ExperimentType.objects.get(code=2),
    status = Status.objects.get(code=2),
    creationDate = timezone.now(),
    projectID = "CC-012345",
    reviewer = "Head Scientist K"
)

ve1.save()
ve2.save()
ve3.save()
