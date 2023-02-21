# Data product specification

Use the `00-specification.yml` file in your data product definition folder to provide an overall title and description for your data product, and tags to help users find it. If you wish, you can also write a short value proposition outling *why* the product exists and what data analysis or visualisation might arise from it.

You should also provide contact information for the product.

## Example

```yaml
specification:
  data-platform.justice.gov.uk/title: "Example Data Product"
  data-platform.justice.gov.uk/description: "Example Data Product contains published prison population from 2001 to present"
  data-platform.justice.gov.uk/product-tags: ["HMPPS", "prisons", "published data", "national statistics"]
  data-platform.justice.gov.uk/value-proposition: "Adding published prison population allows for a reusable, consistent, safely sharable resource for this commonly used data"
  data-platform.justice.gov.uk//limitations:
  data-platform.justice.gov.uk/product-version: 0.0.1
  data-platform.justice.gov.uk/owner-github-team: "data-platform-admins"
  data-platform.justice.gov.uk/type: "dataset"
  support:
    data-platform.justice.gov.uk/owner-email: "data-platform@digital.justice.gov.uk"
    data-platform.justice.gov.uk/owner-ms-teams:
    data-platform.justice.gov.uk/owner-slack-channel: "data-platform"
    data-platform.justice.gov.uk/product-guidance-url:
```

## Notes

### Naming and tagging

The product's `title` must be descriptive and unique - we check for uniqueness when data product requests are created.

> NOTE: the `product-version` attribute is not yet documented here. We are still determining if this should be provided by the data product owner, or automatically incremented when the data dictionary or other metadata is updated.

Product `tags` are an array of strings.

### Contact information

You must supply at least one of the following to indicate ownership of the data product (either email, MS Teams channel or Slack channel):

- `data-platform.justice.gov.uk/owner-email`
- `data-platform.justice.gov.uk/owner-ms-teams`
- `data-platform.justice.gov.uk/owner-slack-channel`

If the preferred contact method is email, please provide a group address or shared mailbox rather than an individual's address.

Important notifications about your data product are sent to the supplied address, so please ensure it is monitored.

### Product type

The `data-platform.justice.gov.uk/type` attributes must be one of the following:

- `dataset`
- `raw-data`
- `data-enhanced-product`
- `derived-data`
- `reports`
- `analytic-view`
- `automated-decsion-making`

We would expect most data products to be of type `dataset`, `raw-data`, or `data-enhanced-product` (the latter typically being a data product derived from another data product). The other types are typically outputs *from* data products, but in some cases you may wish to supply derived or calculated data - for example if the analytics or processing is not currently hosted on the Data Platform.

### Optional attributes

Most of the attributes outlined above are required, however:

- `data-platform.justice.gov.uk//limitations` is optional free text which tells users about what they *can't* or *shouldn't* do with this data
- `data-platform.justice.gov.uk/product-version` is optional, but recommended as we can provide versioned APIs for your data
- `data-platform.justice.gov.uk/owner-github-team` is optional - if provided we can provide more advanced analytics for GitHub users
- `data-platform.justice.gov.uk/product-guidance-url` is optional - if this is provided the data catalogue can link to your guidance (for example a SharePoint page or Google doc)
