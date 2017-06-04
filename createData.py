from datetime import datetime
from django.utils import timezone

from splash.models import Status
from splash.models import ExperimentType
from splash.models import ExperimentDetails
from splash.models import ValaEntry
from splash.models import Equipment
from splash.models import File
from splash.models import FileType

from django.contrib.auth.models import User


def deleteInstances():
    ValaEntry.objects.all().delete()
    Status.objects.all().delete()
    ExperimentType.objects.all().delete()
    ExperimentDetails.objects.all().delete()
    Equipment.objects.all().delete()
    File.objects.all().delete()
    FileType.objects.all().delete()
    User.objects.all().delete()


def createData():
    user1 = User.objects.create_user('gfreeman', 'gfreeman@blackmesa.com', 'gordonpassword')
    user1.first_name = 'Gordon'
    user1.last_name = 'Freeman'
    user1.save()

    user2 = User.objects.create_user('aeinstein', 'aeinsten@ias.edu', 'albertpassword')
    user2.first_name = 'Albert'
    user2.last_name = 'Einstein'
    user2.save()

    user3 = User.objects.create_user('rfeynman', 'rfeynman@losalamos.gov', 'richardpassword')
    user3.first_name = 'Richard'
    user3.last_name = 'Feynman'
    user3.save()

    veStatus0 = Status(code="0", text="New")
    veStatus1 = Status(code="1", text="Pending Review")
    veStatus2 = Status(code="2", text="Completed")
    veStatus3 = Status(code="3", text="Deleted")

    veStatus0.save()
    veStatus1.save()
    veStatus2.save()
    veStatus3.save()

    veEntry0 = ExperimentType(
        code=0,
        name="AST",
    )
    veEntry1 = ExperimentType(
        code=1,
        name="Microcentrifuge Disso"
    )
    veEntry2 = ExperimentType(
        code=2,
        name="Thermal Characterization (DSC)"
    )
    veEntry3 = ExperimentType(
        code=3,
        name="Potency"
    )
    veEntry4 = ExperimentType(
        code=4,
        name="Equilibrium Solubility")
    veEntry5 = ExperimentType(
        code=5,
        name="PXRD"
    )
    veEntry6 = ExperimentType(
        code="6",
        name="NMR Characterization"
    )

    veEntry0.save()
    veEntry1.save()
    veEntry2.save()
    veEntry3.save()
    veEntry4.save()
    veEntry5.save()
    veEntry6.save()

    ft0 = FileType(
        code=0,
        type="csv"
    )

    ft1 = FileType(
        code=1,
        type="xls"
    )

    ft2 = FileType(
        code=2,
        type="sqlite"
    )

    ft3 = FileType(
        code=3,
        type="txt"
    )

    ft4 = FileType(
        code=4,
        type="doc"
    )

    ft0.save()
    ft1.save()
    ft2.save()
    ft3.save()
    ft4.save()

    ve1 = ValaEntry(
        status=Status.objects.get(code=0),
        creationDate=timezone.now(),
        projectID="AA-012345",
        reviewer="Head Scientist B"
    )

    ve2 = ValaEntry(
        status=Status.objects.get(code=1),
        creationDate=timezone.now(),
        projectID="BB-012345",
        reviewer="Head Scientist K"
    )

    ve3 = ValaEntry(
        status=Status.objects.get(code=2),
        creationDate=timezone.now(),
        projectID="CC-012345",
        reviewer="Head Scientist K"
    )

    ve1.save()
    ve1.scientists.add(User.objects.get(id=user1.id))
    ve1.scientists.add(User.objects.get(username='aeinstein'))

    ve2.save()
    ve2.scientists.add(User.objects.get(username=user1.username))
    ve2.scientists.add(User.objects.get(username=user3.username))

    ve3.save()
    ve3.scientists.add(User.objects.get(username=user2.username))
    ve3.scientists.add(User.objects.get(username=user3.username))

    experimentDetails1 = ExperimentDetails(
        valaEntry=ve1,
        hypothesis="This is the first hypothesis",
        experimentType=ExperimentType.objects.get(code=0)
    )

    experimentDetails1.save()

    experimentDetails2 = ExperimentDetails(
        valaEntry=ve2,
        hypothesis="This is the second hypothesis",
        experimentType=ExperimentType.objects.get(code=4)
    )

    experimentDetails2.save()

    experimentDetails3 = ExperimentDetails(
        valaEntry=ve3,
        hypothesis="This is the third hypothesis",
        experimentType=ExperimentType.objects.get(code=2)
    )

    experimentDetails3.save()

    equip1 = Equipment(valaEntry=ve1, equipmentID="BRI-EQ-0001", name="goggles")
    equip2 = Equipment(valaEntry=ve2, equipmentID="BRI-EQ-0002", name="centrifuge")
    equip3 = Equipment(valaEntry=ve3, equipmentID="BRI-EQ-0003", name="flux capacitor")

    equip1.save()
    equip2.save()
    equip3.save()

    file1 = File(
        valaEntry=ve1,
        fileType=ft0,
        description="Data file for an experiment",
        fileID="AABB123",
        name="file1.csv",
    )

    file2 = File(
        valaEntry=ve1,
        fileType=ft1,
        description="Data descriptions",
        fileID="AABB223",
        name="file2.xls",
    )

    file3 = File(
        valaEntry=ve2,
        fileType=ft3,
        description="secret codes",
        fileID="AABB123",
        name="file3.txt",
    )

    file1.save()
    file2.save()
    file3.save()

    print "complete!"


deleteInstances()
createData()
