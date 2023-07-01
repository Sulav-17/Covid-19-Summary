
Select *
From dbo.NashvilleHousing

--------------------------------------------------------------------------------------------

-- Standardize Date Format

Select SaleDateConverted
From dbo.NashvilleHousing

Alter Table NashvilleHousing
Add SaleDateConverted Date;

Update NashvilleHousing
SET SaleDateConverted = Convert(Date, SaleDate)

--------------------------------------------------------------------------------------------

-- Populate Property Address data

Select *
From dbo.NashvilleHousing
--Where PropertyAddress is  null
order by ParcelID


Select HousingA.ParcelID, HousingA.PropertyAddress, HousingB.ParcelID, HousingB.PropertyAddress,
ISNULL(HousingA.PropertyAddress,HousingB.PropertyAddress)
From dbo.NashvilleHousing HousingA
Join dbo.NashvilleHousing HousingB
on HousingA.ParcelID = HousingB.ParcelID
	AND HousingA.[UniqueID] <> HousingB.[UniqueID]
Where HousingA.PropertyAddress is null

Update HousingA
SET PropertyAddress = ISNULL(HousingA.PropertyAddress,HousingB.PropertyAddress)
From dbo.NashvilleHousing HousingA
Join dbo.NashvilleHousing HousingB
on HousingA.ParcelID = HousingB.ParcelID
	AND HousingA.[UniqueID] <> HousingB.[UniqueID]
	Where HousingA.PropertyAddress is null


---------------------------------------------------------------------------------

-- Broke out Address to state, city, street

Select PropertyAddress
From dbo.NashvilleHousing
--Where PropertyAddress is  null
--order by ParcelID

Select 
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1) as Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyADDress)) as Address
From dbo.NashvilleHousing


Alter Table NashvilleHousing
Add PropertySplitAddress Nvarchar(255);

Update NashvilleHousing
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1)


Alter Table NashvilleHousing
Add PropertySpilitcity Nvarchar(255);

Update NashvilleHousing
SET PropertySpilitcity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyADDress))



Select OwnerAddress
From dbo.NashvilleHousing

Select 
PARSENAME(REPLACE(OwnerAddress, ',','.'),3)
,PARSENAME(REPLACE(OwnerAddress, ',','.'),2)
,PARSENAME(REPLACE(OwnerAddress, ',','.'),1)
From dbo.NashvilleHousing



Alter Table NashvilleHousing
Add OwnerSplitAddress Nvarchar(255);

Update NashvilleHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',','.'),3)


Alter Table NashvilleHousing
Add OwnerSpilitcity Nvarchar(255);

Update NashvilleHousing
SET OwnerSpilitcity = PARSENAME(REPLACE(OwnerAddress, ',','.'),2)


Alter Table NashvilleHousing
Add OwnerSpilitState Nvarchar(255);

Update NashvilleHousing
SET OwnerSpilitState = PARSENAME(REPLACE(OwnerAddress, ',','.'),1)



--------------------------------------------------------------
---Change 'Y' / 'N' to yes/no

Select Distinct(SoldAsVacant), Count(SoldAsVacant)
From dbo.NashvilleHousing
Group by SoldAsVacant
Order by 2



Select SoldAsVacant
, Case When SoldAsVacant = 'Y' Then 'Yes'
		When SoldAsVacant = 'N' Then 'No'
		Else SoldAsVacant
		END
From dbo.NashvilleHousing


Update NashvilleHousing
SET SoldAsVacant = Case When SoldAsVacant = 'Y' Then 'Yes'
						When SoldAsVacant = 'N' Then 'No'
						Else SoldAsVacant
						END


----------------------------------------------------------------------------

-- Delete Unused Columns 

Select *
From dbo.NashvilleHousing

Alter Table dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate