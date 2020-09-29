### the graphql story so far

- unadorned retrieval of `tag`, `tags`, `entry`, `entries`

This is enough to start work on the `Vue` part.

### what's missing
- no sorting yet
- no filtering yet
- no pagination yet

I need both of these to do filtered, paginated lists of `entries` and `tags`.

- I want a paginated list of all `entries` sorted by `slug`.
- I want a paginated list of all `entries` with tag `x` sorted by `slug`.
- I want a paginated list of all `tags` sorted by `slug`.
- I *only somewhat* want a paginated 
list of all `entries` sorted by `dateEdit`.
- I *only somewhat* want a paginated 
list of all `entries` with tag `x` sorted by `dateEdit`.


### what is pagination anyway

Applies to `tags` and `entries`

- set an overrideable default value (`paginateBy:50`)
- what are the items on page `x`?
    - get by Python slice
- is there a next page?
    - If so, I can calculate its coordinates in the `Vue` layer
- is there a previous page?
    - If so, I can calculate its coordinates in the `Vue` layer
- how many pages are there? (`pageCount`)
- how many items are there? (`itemCount`)

Ss it stands, `graphene-django-extras`
isn't enough to get me this, or it is but 
in an undocumented way.

# PaginatingList

## `tags`

- `pageNum` (defaults to `null` meaning return all items)
- `paginateBy` (defaults to `50`)

## `entries`

- `pageNum` (defaults to `null` meaning return all items)
- `paginateBy` (defaults to `50`)
- `ordering` (one field name, or more?) `slug` `dateEdit`
- `tag` (tag to filter by, default `null`)

## fields in `pagingInfo`
 
if `pageNum` wasn't `null`

- `hasNext`, `hasPrev`: booleans
- `totalPages`
- `totalItems`

# query and response: entry

```
{
  entry(slug: "zero") {
    name
    slug
    text
    dateCreate
    dateEdit
    tags {
      name
      slug
    }
  }
}
```
returns
```json
{
  "data": {
    "entry": {
      "name": "zero",
      "slug": "zero",
      "text": "## what you should know\r\n\r\nMuch ado, you could say.",
      "dateCreate": "2020-02-24T20:20:07.027536+00:00",
      "dateEdit": "2020-02-24T21:17:54.891114+00:00",
      "tags": [
        {
          "name": "glossary",
          "slug": "glossary"
        },
        {
          "name": "number theory",
          "slug": "number-theory"
        }
      ]
    }
  }
}
```