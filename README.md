# SQL-extractor
Utility for helping with SQL-Databases



## Commands
### print-create-table
Print SQL for creating the table.
```
python sql_extractor.py --dialect tsql --connection-string local:AdventureWorks print-create-table --table Person.BusinessEntity

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Person].[BusinessEntity](
    [Id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
    [rowguid] [uniqueidentifier] NOT NULL,
    [ModifiedDate] [datetime] NOT NULL
) ON [PRIMARY]
GO
```

### print-insert
Print SQL "template" for inserting new data to table.
```
python sql_extractor.py --dialect tsql --connection-string local:AdventureWorks print-insert --table Person.BusinessEntity

INSERT INTO [Person].[BusinessEntity] ([Id], [rowguid], [ModifiedDate])
     VALUES
    (
          -- Id, int
         ,-- rowguid, uniqueidentifier
         ,-- ModifiedDate, datetime
    )
GO
```

### print-table-structure
Print table structure either as markdown or as HTML
```
python sql_extractor.py --dialect tsql --connection-string local:AdventureWorks print-table-structure --table Person.BusinessEntity --format md

## BusinessEntity
| Name | Type |
| ------------- |:----- |
| Id | int |
| rowguid | uniqueidentifier |
| ModifiedDate | datetime |
```

## TODO
- Add support for postgresql
- Output table relations as dot-file
- Insert test data into DB according to table-relations

## Dev
### Install according to poetry.lock
- `poetry install`

### Launch shell
- `poetry shell`

### Running tests
- `python -m unittest discover`







