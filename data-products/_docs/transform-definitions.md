# Describing data transformations

When describing what has happened to your data before users get to interact with it, you should describe any data transformations you have used. Transforms should be documented in the `03-transformations.yml` file in your data product definition folder.

See also our guidance on describing [data cleaning](./cleansing-definitions.md) your data may have applied to it.

## Types of data transformation

These have been derived from the contributions made to the [Data Management Wiki](https://datamanagement.wiki/data_quality_management_system/data_cleansing). <!--Some of these contain US spellings - we also accept the UK equivalent (for example "normalisation" and "normalization" are both accepted).-->

Please use the identifier (ID) for the transformation types when populating your `03-transformations.yml` file.

| ID                  | Method             | Description                                                                                                                                                                                                                                                                                         |
| ------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clustering          | Clustering         | Clustering is a classic data mining technique based on machine learning that divides ​groups of abstract objects into classes of similar objects. Clustering helps to split data into several subsets.                                                                                              |
| denormalisation     | Denormalisation    | Denormalisation is a formal technique that increases data redundancy but can improve usability in some circumstances. Typically this refers to replacing reference codes or IDs with their actual value. The opposite of normalisation.                                                             |
| enhancement         | Data enhancement   | Enhancement is the process that expands existing data with data from other sources (enrichment). Here, additional data is added to close existing information gaps.                                                                                                                                 |
| harmonisation       | Data harmonisation | Data harmonisation is the process of bringing together your data of varying file formats, naming conventions, and columns, and transforming it into one cohesive data set.                                                                                                                          |
| normalisation       | Normalisation      | Normalisation is a formal technique that eliminates the data redundancy in a number of steps (= normal forms) by splitting the data according to fixed rules. The opposite of denormalisation.                                                                                                      |
| merging             | Merging            | The merging of two or more datasets because they are fundamentally similar, or make more logical sense to a user when combined.                                                                                                                                                                     |
| standardisation     | Standardisation    | Standardisation transforms data into a standard form - for example if the same information is represented slightly differently across different systems, you may wish to standardise those values so they match with other data products. Standardisation is also permissible as a cleaning method. |
| statistical-methods | Statstical methods | Statistics is the science and technique of collecting, processing, interpreting and presenting data based on rules of mathematics and the laws of logic. Statistical methods include regression, correlation, min, max, standard deviation, mean and clustering.                                    |
| selection           | Selection          | Selection is when you choose to only provide a subset of your data - please clearly describe what is and isn't included, and your reasoning for this.                                                                                                                                               |

### Data with no transformations applied

If your data has not undergone any transformation, we suggest you explicitly inform users of this by adding `type: none` for each of your tables to make this clear to users.

## Considerations

Carefully consider if transformations are enhancing the data product for general use, rather than for a single use case.

<!--## Template generation

Our roadmap contains plans for tools to aid in template generation - for example generating a skeleton `03-transformations.yml` given a `02-data-dictionary.yml` as input.-->

## Suggesting changes

If you wish to suggest additions or improvements to the cleansing types, please [follow our guidance](https://github.com/ministryofjustice/data-platform-products) on submitting a pull request.

## Further reading

[Index of documention for data product defintion](../README.md#defining-a-data-product)

[Example data product](../_example/)
