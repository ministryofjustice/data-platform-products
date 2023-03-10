# The data dictionary

The `02-data-dictionary.yml` file should contain a detailed specification of the structure of the data in YAML format. Like most schemas, we require that you supply

- table names, column names and column types (for tabular data);
- or domains, classes and attributes (for domain modelled data)

**Unlike** some other schemas, we also ask that you **describe** the components of the data so that users understand what they are.

## Top-level attributes

The overall data dictionary requires these top-level attributes:

```yaml
default:
  model: "tabular"
  description: "Extracted from the Offender Management Statistics Quarterly publication. Please refer to notes in that publication."
  limitations: { free text }
  enable-versioning: false
```

The top-level attribute ("`default`" in the above example) defines a group or collection of datasets. In most cases you will have only one collection, so we recommend you use the data product name.

- `model` - allowable values are `tabular` or `domain` (default is "tabular")
- `description` - optional free text to help users find the data. Useful if you have more than one group and you want to enhance the description provided by the overall data product specification
- `limitations` - optional free text to enhance any particular limitations of a group of data, in addition to any limitations provided by the overall data product specification
- `enable-versioning` - allowable values are true or false (default false). If versioning is enabled, the Data Platform will store a historical snaphot of the database each time an update is sent. This can add SIGNIFICANTLY to storage costs, so you may be asked to justify this.

## Table and column attributes

The `tables` attribute is contained within the top-level group, and contains a list of table names (without spaces). Additional attributes are defined for the table including a user-friendly description and an update strategy (more on this below). Each table then contains a collection of columns with attributes to define each column.

### Example

```yaml
tables:
  population_by_offence:
    description: "Prison population by offence group"
    update-strategy: "all-dimensions"
    columns:
      # A column must contain at least a name and a data type.
      - name: "Offence"
        description: "Offence group"
        data-type: "string"
        column-type: "dimension"
        # e.g. reference data - a table in this database or the URI of a table in another product
        reference-table: "offence_groups"
      - name: "Date"
        data-type: "date"
        column-type: "dimension"
        primary-period: true
      - name: "Population"
        data-type: "int"
        column-type: "fact"
```

This defines one table called "population_by_offence", with three columns - "Offence", "Date", and "Population". In general, a column will have the following attributes:

- `name` - the name of the column as seen by users. This should be kept relatively short, and we suggest avoiding spaces or hyphens
- `description` - additonal free text information about the column
- `data-type` - one of `string`, `int` (integer), `float`, `decimal`, `bit` (boolean), `date`, `time`, or `datetime`
- `column-type` - either `fact` or `dimension`. In this case the "fact" is the numeric value for prison population, and the two dimensions are "Offence" and "Date". So a user could use the dimension values "Theft offences" and "31st Dec 2022" to find a particular prison population value (fact) - 758 ([source](https://www.gov.uk/government/statistics/offender-management-statistics-quarterly-july-to-september-2022)).
- `reference-table` is optional for dimension columns. If the dimension contains a code or ID which refers to a lookup table, the name of that table should be supplied here. The reference table must contain a matching column - by name and type - on which to perform joins and lookups.

### Dates and "primary period" columns

For data with a time dimension (for example a date column), we can enforce retention periods and inform users of the range of available data. This is specified using the `primary-period` attribute, with a value of `true`.

For a more complete example, see [02-data-dictionary](../_example/02-data-dictionary.yml) in the example data product.

## Update strategies

When sending updates to data to the platform, we need to know how to replace or insert data. This is done using the `update-strategy` attribute, which supports two options:

- `all-dimensions` or;
- `selected-dimensions`

When `all-dimensions` is specified, data will be updated or inserted based on all the columns which are defined as `column-type: "dimension"`. For example if new data is sent to the table defined above, any existing values (facts) will be ovewritten if the offence and date matches existing data, or new records will be added if a matching combination of offence and date is not found.

When `selected-dimensions` is specified, you must also supply an array of update key dimensions. For example:

```yaml
tables:
  population_by_age:
    description: "Prison population by age band"
    update-strategy: "selected-dimensions"
    update-dimensions: ["date"]
```

In this case, an update will overwrite all values based on just the date column, regardless of the "age" dimension. Column(s) specified in the `update-dimensions` array must exist in the table.

If `update-strategy` is omitted, the platform assumes the `all-dimensions` strategy should be used.

## Schema generation articles and utilities

You can generate your initial data dictionary by hand, or use a tool. Here we link to a few tools. Most of these will generate a JSON schema - the Data Platform format is YAML since it strikes a nice balance between machine and human readability, and is (arguably) easier to hand edit.

You can find utilities to generate YAML from JSON, since one is a subset of the other - for example here is one [browser based tool](https://www.json2yaml.com/).

Our favourite tool for editing YAML is [Visual Studio Code](https://code.visualstudio.com/) with the [YAML plugin](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml).

### PostgreSQL

[A Stack Overflow article](https://stackoverflow.com/questions/22272855/convert-a-postgres-db-schema-to-a-json-format)

### Microsoft SQL Server

[An MSSQL Tips article on using SQL to generate a JSON schema](https://www.mssqltips.com/sqlservertip/6270/save-sql-server-database-structure-as-json/)

### Oracle

We havent yet found a JSON schema generator for Oracle - please let us know if you know of one (or want to create one!). The SQL Server approach above may be adaptable to Oracle.

## Further reading

[Index of documention for data product defintion](../README.md#defining-a-data-product)

[Example data product](../_example/)
