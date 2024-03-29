# Describing data cleansing

When describing what has happened to your data before users get to interact with it, you should describe any data cleaning processes which you have used, either at a table or column level. Cleansing should be documented in the `03-transformations.yml` file in your data product definition folder.

See also our guidance on describing [transformations](./transform-definitions.md) your data may have applied to it.

## Types of data cleansing

These have been derived from the contributions made to the [Data Management Wiki](https://datamanagement.wiki/data_quality_management_system/data_cleansing). <!--Some of these contain US spellings - we also accept the UK equivalent (for example "normalisation" and "normalization" are both accepted).-->

Please use the identifier (ID) for the cleaning types when populating your `03-transformations.yml` file.

| ID                            | Method                                   | Description                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| abbreviation-expansion        | Abbreviation expansion                   | Abbreviation expansion transforms abbreviations into their full form. There are different kinds of abbreviation. These can be shortened words such as "mgmt", or acronyms, where the abbreviation consists of a prefix of the original data value. E.g. "MDT" stands for "mandatory drug testing". |
| cross-checking                | Cross-checking with a validated data set | Some data cleansing solutions will clean data by cross-checking with a validated data set. In these cases you should reference the dataset used for cross-checking.                                                                                                                                |
| correct-typos                 | Correct typographical errors             | A typographical error (often shortened to typo), is a mistake (such as a spelling mistake) made in the data                                                                                                                                                                                        |
| drop-or-impute-missing-values | Drop or impute missing values            | Missing values are data or data points of a variable that are missing. Missing data are a common occurrence and can have a significant effect on the conclusions that can be drawn from the data.                                                                                                  |
| group-duplicates              | Group duplicates                         | Duplicates are data points that are repeated in your dataset. Every duplicate detection method proposed requires an algorithm for determine whether two or more records are duplicate representations of the same entity.                                                                          |
| parsing                       | Parsing                                  | Parsing is a method where one string of data gets converted into a different type of data. Parsing in data cleansing is performed for the detection of syntax errors.                                                                                                                              |
| remove-duplicates             | Remove duplicates                        | Duplicates are data points that are repeated in your dataset. Every duplicate detection method proposed requires an algorithm for determine whether two or more records are duplicate representations of the same entity.                                                                          |
| remove-inconsistency          | Remove inconsistency                     | Data inconsistency is a condition that occurs between tables when we keep similar data in different formats in two different tables. Data inconsistency creates unreliable information, because it will be difficult to determine which version of the information is correct.                     |
| remove-irrelevant-data        | Remove irrelevant data                   | Irrelevant data are the data that are not actually needed, and don’t fit under the context of the problem we’re trying to solve.                                                                                                                                                                   |
| remove-outliers               | Remove outliers                          | Outliers are values that are significantly different from all other observations. They should not be removed unless there is a good reason for that, since users may need to see them.                                                                                                             |
| standardisation               | Standardisation                          | Standardisation transforms data into a standard form - for example if the same information is represented slightly differently across different systems, you may wish to standardise those values so they match with other data products.                                                          |
| statistical-methods           | Statistical methods                      | Statistical methods are used to identify data issues and provide cleaning or flagging of data issues.                                                                                                                                                                                              |
| suppress-small-values         | Suppress small values                    | Suppression is when small values are removed are replaced to avoid identifying individuals.                                                                                                                                                                                                        |
| redaction                     | Redaction                                | Redaction is the removal of sensitive or other restricted information.                                                                                                                                                                                                                             |
| type-conversion               | Type conversion                          | Type conversion (also called casting) is an operation that converts a piece of data of one data type to another data type. Type conversion can be used to make sure that numbers are stored as numerical data types and that a date should be stored as a date object.                             |

## Examples

You have a table called `prison_releases` defined in `02-data-dictionary.yml` which contains anonymised, row-level data from a case management system about individuals released from prison. Since an individual can be "released" from more than one prison sentence at the same time, or because of data entry errors, the raw data may appear to, or actually, contain duplicates. You know your users only want a single record per release, so you choose to de-duplicate the data by deleting all but one instance of each duplicate. This is a table level cleaning process which would be documented in `03-transformations.yml` like this:

```yaml
cleansing:
  prison_releases:
    - type: "remove-duplicates"
      description: "Duplicate releases removed by choosing the duplicate with the highest numbered record ID and discarding the others"
```

Your users aren't happy with that, so instead you apply a `GROUP BY` to your dataset, so that there is only one row per release but you retain information which may otherwise be lost:

```yaml
cleansing:
  prison_releases:
    - type: "group-duplicates"
      description: "Duplicate releases removed by concatenating multiple sentences into one string"
```

Multiple cleaning steps can be added, so for example you might want to clearly show any enhancements you added as part of the above `group-duplicates`:

```yaml
cleansing:
  prison_releases:
    - type: "group-duplicates"
      description: "Duplicate releases removed by concatenating multiple sentences into one string"
    - type: "data-enhancement"
      description: "Add a flag column to indicate which records were affected by the de-duplication process"
```

Furthermore, there may be a column of data which contains jargon or abbrevations which you wish to make more user-friendly. Assuming you cannot take the preferred approach of providing a reference table for this, you may decide to expand or replace these as part of your cleansing. For example there's a column which contains some information about whether the release was early, on time, or late, but users of the case management system have taken to entering "E", "OT", "L", "VL", and there's no reference data or data entry validation for this. You use your knowledge of the system to provide an enhancement to expand those abbreviations.

```yaml
cleansing:
   prison_releases:
     - type: "group-duplicates"
       description: "Duplicate releases removed by concatenating multiple sentences into one string"
     - type: "data-enhancement"
       description: "Add a flag column to indicate which records were affected by the de-duplication process"
     columns:
       timely_release:
         - type: "abbreviation-expansion"
           description: "Replace data entry shorthand with expanded text (e.g. 'VL' => 'very late'); or 'unknown'"
```

Our [example data product](./_example/) contains a few more examples.

### Data with no cleansing applied

If your data has not undergone any cleansing, we suggest you explicitly inform users of this by adding `type: none` to make this clear to users. Otherwise we will assume there has been undocumented cleansing. An exception is made for tables [defined as reference data](./_example/02-data-dictionary.yml#L67) - here we assume no cleansing has been applied if there is no cleansing specified.

## Considerations

Wherever possible, it is better to have clean data captured at source. If you are regularly applying certain types of cleaning, consider whether it is possible and practical for additional data validation to be added to the originating system(s).

<!--## Template generation

Our roadmap contains plans for tools to aid in template generation - for example generating a skeleton `03-transformations.yml` given a `02-data-dictionary.yml` as input.-->

## Suggesting changes

If you wish to suggest additions or improvements to the cleansing types, please [follow our guidance](https://github.com/ministryofjustice/data-platform-products) on submitting a pull request.

## Further reading

[Index of documention for data product defintion](../README.md#defining-a-data-product)

[Example data product](../_example/)
