# Data product specification

Use the `00-specification.yml` file in your data product definition folder to provide a name, title and description for your data product, and tags to help users find it. If you wish, you can also write a short value proposition outling _why_ the product exists and what data analysis or visualisation might arise from it. In general, the `00-specification.yml` file contains information that users of the data will see.

You should also provide contact information for the product.

## Example

```yaml
specification:
  data-platform.justice.gov.uk/name: "_example"
  data-platform.justice.gov.uk/title: "Example Data Product"
  data-platform.justice.gov.uk/description: "Example Data Product contains published prison population from 2001 to present"
  data-platform.justice.gov.uk/product-tags: ["HMPPS", "prisons", "published data", "national statistics"]
  data-platform.justice.gov.uk/value-proposition: "Adding published prison population allows for a reusable, consistent, safely sharable resource for this commonly used data"
  data-platform.justice.gov.uk/status: "production"
  data-platform.justice.gov.uk//limitations:
  data-platform.justice.gov.uk/product-version: 0.0.1
  management:
    data-platform.justice.gov.uk/owner-aad-group: "data-platform-admins"
    data-platform.justice.gov.uk/owner-github-team: "data-platform-admins"
  support:
    data-platform.justice.gov.uk/owner-email: "data-platform@digital.justice.gov.uk"
    data-platform.justice.gov.uk/owner-ms-teams:
    data-platform.justice.gov.uk/owner-slack-channel: "data-platform"
    data-platform.justice.gov.uk/product-guidance-url:
```

## Notes

### Naming and tagging

The product's `name` must be reasonably short and unique - we check for uniqueness when data product requests are created. This is because:

- The product name is a directory in the data products repository. E.g. 'your_data_product' becomes `./data_products/your_data_product/`
- It will be the root of the API endpoint `https://data-platform.service.justice.gov.uk/api/your-data-product/`

You must only use alphanumeric characters or underscores. Don't use spaces - we will replace spaces with underscores.

The product `title` should be the human-readable version of the name. Keep it short but meaningful. We suggest product titles are unique, since:

- Users may see it listed in a directory of products, and multiples of the same title are confusing
- Users may know a product title well enough to search for it directly

The product `description` can be longer, give more information and will help users find your data.

> NOTE: the `product-version` attribute is not yet documented here. We are still determining if this should be provided by the data product owner, or automatically incremented when the data dictionary or other metadata is updated.

Product `tags` are an array array of quoted strings to further aid discoverability (think of them as search keywords).

### Management access

Using the `management` attribute, you must supply the name of a group of users who will have permisson to manage this data product. Use either (or both) of the following:

- `data-platform.justice.gov.uk/owner-aad-group` - the name of a Azure Active Directory (AAD) security group
- `data-platform.justice.gov.uk/owner-github-team` - the name of a GitHub team

Note these are **groups** of users, not the name of an individual.

### Contact information

You must supply at least one of the following to indicate ownership of the data product (either email, MS Teams channel or Slack channel):

- `data-platform.justice.gov.uk/owner-email`
- `data-platform.justice.gov.uk/owner-ms-teams`
- `data-platform.justice.gov.uk/owner-slack-channel`

If the preferred contact method is email, please provide a group address or shared mailbox rather than an individual's address.

Important notifications about your data product are sent to the supplied address, so please ensure it is monitored.

<!--
### Product type

The `data-platform.justice.gov.uk/type` attributes must be one of the following:

- `dataset`
- `raw-data`
- `data-enhanced-product`
- `derived-data`
- `reports`
- `analytic-view`
- `automated-decsion-making`

We would expect most data products to be of type `dataset`, `raw-data`, or `data-enhanced-product` (the latter typically being a data product derived from another data product). The other types are typically outputs _from_ data products, but in some cases you may wish to supply derived or calculated data - for example if the analytics or processing is not currently hosted on the Data Platform.

-->

### Optional attributes

Most of the attributes outlined above are required, however:

- `data-platform.justice.gov.uk/limitations` is optional free text which tells users about what they _can't_ or _shouldn't_ do with this data. If your data product has undergone a Data Protection Impact Assesment (DPIA) which highlights inappropriate use cases, you should list those here.
  - > NOTE: if your data product is still in development, or has draft status, please flag this using the `status` attribute described below
- `data-platform.justice.gov.uk/owner-github-team` is optional - if provided we can provide more advanced analytics for GitHub users
- `data-platform.justice.gov.uk/product-guidance-url` is optional - if this is provided the data catalogue can link to your guidance (for example a SharePoint page or Google doc)

### Product status

- `data-platform.justice.gov.uk/status`: use one of the following to indicate to users the status of the data:
  - `draft`
  - `development`
  - `testing`
  - `production`
  - `sunset`
  - `retired`

Most data products will be tagged as `production` - the other statuses will flag to users that special handling is required. If `status` is omitted, we assume it is `production`.

## Further reading

[Index of documention for data product defintion](../README.md#defining-a-data-product)

[Example data product](../_example/)
