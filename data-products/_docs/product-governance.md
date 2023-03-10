# Defining data product governance

The purpose of the `01-governance.yml` file in your data product definition folder is to indicate to users, and to the data platform itself, how the data should be handled, and where it has come from. A correctly specficied set of governance attributes gives you and platform users confidence in handling and using the data.

## Example

```yaml
governance:
  data-platform.justice.gov.uk/data-controller: "moj"
  data-platform.justice.gov.uk/review-after: "2023-12-31"
  data-platform.justice.gov.uk/senior-information-risk-owner: "information.asset.owner.name@justice.gov.uk"
  data-platform.justice.gov.uk/protective-marking: "None"
  update-frequency:
    data-platform.justice.gov.uk/update-unit: "months"
    data-platform.justice.gov.uk/update-value: 3
  retention:
    data-platform.justice.gov.uk/retention-strategy: "forever"
    data-platform.justice.gov.uk/retention-unit: "years"
    data-platform.justice.gov.uk/retention-value: 25
  lineage:
    data-platform.justice.gov.uk/organisational-unit: "HMPPS"
    data-platform.justice.gov.uk/source: "https://www.gov.uk/government/collections/offender-management-statistics-quarterly"
    data-platform.justice.gov.uk/parent-products: ["parent_product", "other_parent_product"]
```

## Notes

### Ownership and handling attributes

- `data-platform.justice.gov.uk/data-controller` is the Data Controller as pertains to the Data Protection Act. This will commonly be "moj" but could be another entity.
- `data-platform.justice.gov.uk/review-after` - on which date should the governance information be reviewed. Data products owners will be notified of this review window using the contact information supplied in the [data product specification](product-specification.md).
- `data-platform.justice.gov.uk/senior-information-risk-owner` should be the email address of the Senior Information Risk Owner for this data.
- `data-platform.justice.gov.uk/protective-marking` - one of "Official", "Official Sensitive", or "None" (for published data). DO NOT SEND SECRET OR TOP SECRET DATA TO THE PLATFORM.

### Data retention

You should indicate to the platform how long the data should be kept before removal using the `data-platform.justice.gov.uk/retention-strategy` attribute. Data retention supports two strategies:

- `date-uploaded` - the retention period is based on the date & time the data was added to the platform; or
- `data-date-key` - the retention period is based on dates within the data itself. For this strategy the [data dictionary](data-dictionary.md) must contain key date fields for all datasets.

For these strategies, you must also supply a time unit and values. Supported values for `retention-unit` are:

- `months`
- `years`

The `retention-value` should be a whole number indicating how many of the `retention-unit` elapses before the retention policy is applied. For example:

```yaml
retention:
  data-platform.justice.gov.uk/retention-strategy: "data-date-key"
  data-platform.justice.gov.uk/retention-unit: "years"
  data-platform.justice.gov.uk/retention-value: 3
```

Would be implemented as _"delete any data older than 3 years, based on the date field for each table"_.

You can also specify `forever` for data which is allowed to be kept indefinitely - for example anonymised management information or published statistics. If `forever` is specified, the `retention-unit` and `retention-value` values are ignored - they are included above to provide a more complete example.

Data products owners will be notified of retention policies being applied using the contact information supplied in the [data product specification](product-specification.md).

### Data updates

You should indicate to the platform, and to users, how frequently the data will be updated using the `update-frequency` attribute. This requires two values:

- `data-platform.justice.gov.uk/update-unit`
- `data-platform.justice.gov.uk/update-value`

Supported values for `update-unit` are:

- `days`
- `weeks`
- `months`

The `update-value` should be a whole number indicating how many of the `update-unit` will elapse before the next upate is sent. For example:

```yaml
update-frequency:
  data-platform.justice.gov.uk/update-unit: "months"
  data-platform.justice.gov.uk/update-value: 3
```

Would be implemented as _"new data will be supplied every three months"_. We don't support multiples of years, but a dataset with annual updates can be specified as having a 12 month update cycle.

If a data update cycle is missed, data product owners will be notified via the contact information supplied in the [data product specification](product-specification.md).

### Data lineage

It is important to users of the data that they know where it has come from. This is the purpose of the `lineage` collection of attributes. These attributes are generally free text, so you are free to interpret their usage in the way you think is most helpful to users.

- `data-platform.justice.gov.uk/organisational-unit` defines at a high level which part of the organisation the data has come from. For example "HMCTS", "HMPPS", "LAA", "OPG", "HQ"
- `data-platform.justice.gov.uk/source` - the detailed source of the data. Can be a system such as "NOMIS" or "XHIBIT" or the URL of a statistical publication
- \- **OR** \-
- `data-platform.justice.gov.uk/parent-products` - if your data product is based on another data product(s), please specify their name here. (The "name" as it appears in the list of data platform product folders, not the user-friendly title of the product).

Note if `parent-product` is supplied then `source` is ignored.

### Other attributes

- `data-platform.justice.gov.uk/status`: use one of the following to indicate to users the status of the data:
  - `draft`
  - `development`
  - `testing`
  - `production`
  - `sunset`
  - `retired`

Most data products will be tagged as `production` - the other statuses will flag to users than special handling is required.

<!-- `data-platform.justice.gov.uk/status`: use one of "draft", "development", "testing", "production", "sunset", "retired" to indicate to users the status of the data. Can be used in conjunction with `data-platform.justice.gov.uk/allow-derived-products` for non-production data.
- `data-platform.justice.gov.uk/allow-derived-products` - typically "true" (and "true" if not supplied), but in some cases you may not wish derived products to be created. If the product status attribute is "production", you may be asked to justify disallowing derived products as we want to encourage data reuse. -->

## Further reading

[Index of documention for data product defintion](../README.md#defining-a-data-product)

[Example data product](../_example/)
