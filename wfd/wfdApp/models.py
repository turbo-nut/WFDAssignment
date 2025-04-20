from django.db import models

# Create your models here.


class Item(models.Model):
    itemID = models.IntegerField(primary_key=True, name="ItemID")
    stock = models.IntegerField(name="stock")
    category = models.CharField(name="category", max_length=50)
    itemName = models.CharField(name="itemName", max_length=20)
    desc = models.CharField(name="desc", max_length=100)
    retailPrice = models.FloatField(name="RetailPrice")


class StaffMember(models.Model):
    staffID = models.IntegerField(primary_key=True, name="StaffID")
    firstName = models.CharField(name="First Name", max_length=10)
    lastName = models.CharField(name="Last Name", max_length=20)


class ShiftManager(models.Model):
    staffID = models.ForeignKey(
        StaffMember, primary_key=True, on_delete=models.CASCADE, related_name='staffID')
    fName = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, related_name='shiftManager-FirstName+', max_length=10)
    lName = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, related_name='shiftManager-LastName+', max_length=20)

    class Meta:
        permissions = [
            ("edit stock", "can edit stock of items")
        ]


class generalManager(models.Model):
    managerID = models.IntegerField(primary_key=True, name="ManagerID")
    foreName = models.ForeignKey(
        StaffMember, related_name='generalManager-FirstName+', on_delete=models.CASCADE, max_length=10)
    surName = models.ForeignKey(
        StaffMember, related_name='generalManager-LastName+', on_delete=models.CASCADE, max_length=20)


class Request(models.Model):
    requestID = models.IntegerField(primary_key=True, name="RequestID")
    managerID = models.ForeignKey(
        generalManager, name="ManagerID", on_delete=models.CASCADE)
    staffID = models.ForeignKey(
        StaffMember, name="StaffID", on_delete=models.CASCADE)
    itemID = models.ForeignKey(Item, name="ItemID", on_delete=models.CASCADE)
    requestDate = models.DateField(name="Request Date")
    reqComments = models.TextField(name="Comments", max_length=50)


class newItemRequest(models.Model):
    requestID = models.ForeignKey(
        Request, primary_key=True, name="RequestID", on_delete=models.CASCADE)
    managerID = models.ForeignKey(
        generalManager, name="ManagerID", on_delete=models.CASCADE)
    staffID = models.ForeignKey(
        StaffMember, name="StaffID", on_delete=models.CASCADE)
    itemID = models.ForeignKey(
        Item, related_name="newItem-ItemID+", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Item, related_name="newitem-Category+", on_delete=models.CASCADE)
    requestDate = models.DateField(name="Request Date")
    reqComments = models.TextField(name="Comments")


class editRequest(models.Model):
    requestID = models.ForeignKey(
        Request, primary_key=True, name="RequestID", on_delete=models.CASCADE)
    itemID = models.ForeignKey(Item, name="ItemID", on_delete=models.CASCADE)
    requestDate = models.DateField(name="Request Date")
    newStock = models.IntegerField(name="New Stock")
    reqComments = models.TextField(name="Comments")


class deletionRequest(models.Model):
    requestID = models.ForeignKey(
        Request, primary_key=True, name="RequestID", on_delete=models.CASCADE)
    itemID = models.ForeignKey(Item, name="ItemID", on_delete=models.CASCADE)
    requestDate = models.DateField(name="Request Date")
    reqComments = models.TextField(name="Comments")
