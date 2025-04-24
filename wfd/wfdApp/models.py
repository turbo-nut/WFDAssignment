from django.db import models

# Create your models here.


class Item(models.Model):
    itemID = models.IntegerField(primary_key=True, name="ItemID")
    stock = models.IntegerField(name="Stock")
    category = models.CharField(name="Category", max_length=50)
    itemName = models.CharField(name="ItemName", max_length=50)
    retailPrice = models.IntegerField(name="RetailPrice")

    def __str__(self):
        return self.ItemName


class StaffMember(models.Model):
    staffID = models.IntegerField(primary_key=True, name="StaffID")
    firstName = models.CharField(name="First Name", max_length=50)
    lastName = models.CharField(name="Last Name", max_length=50)


class ShiftManager(models.Model):
    staffID = models.ForeignKey(
        StaffMember, primary_key=True, on_delete=models.CASCADE, related_name='staffID')
    fName = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, related_name='shiftManager-FirstName+')
    lName = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, related_name='shiftManager-LastName+')
    hasManagerAction = models.BooleanField(default=False)


class generalManager(models.Model):
    managerID = models.IntegerField(primary_key=True, name="ManagerID")
    foreName = models.ForeignKey(
        StaffMember, related_name='generalManager-FirstName+', on_delete=models.CASCADE)
    surName = models.ForeignKey(
        StaffMember, related_name='generalManager-LastName+', on_delete=models.CASCADE)
    isManager = models.BooleanField(default=True)


class Request(models.Model):

    REQ_TYPES = (
        ("DELETION", "Deletion"),
        ("ADDITION", "Addition"),
        ("EDITING", "Editing"),
    )

    requestID = models.IntegerField(primary_key=True, name="RequestID")
    itemName = models.ForeignKey(
        Item, name="ItemName", null=True, on_delete=models.CASCADE)
    requestDate = models.DateField(name="RequestDate")
    newStock = models.IntegerField(name="NewStock", null=True)
    reqType = models.CharField(
        choices=REQ_TYPES, max_length=20, default="Editing")
    reqComments = models.TextField(name="Comments")
