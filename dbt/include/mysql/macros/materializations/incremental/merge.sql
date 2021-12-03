{% macro mysql_get_merge_sql(target, source, unique_key, dest_columns) -%}

  {%- set dest_cols_csv = dest_columns | map(attribute="quoted") | join(", ") -%}

  insert into {{ target }} ({{ dest_cols_csv }})
  (
     select {{ dest_cols_csv }}
     from {{ source }}
  )
  on duplicate key update
  {% for column_name in dest_columns %}
    {{ column_name.quoted }} = {{ source }}.{{ column_name.quoted }}
    {%- if not loop.last %}, {%- endif %}
  {%- endfor %}

{% endmacro %}

{% macro mysql__get_delete_insert_merge_sql(target, source, unique_key, dest_columns) -%}

  {%- set dest_cols_csv = get_quoted_csv(dest_columns | map(attribute="name")) -%}

  {% if unique_key is not none %}
  delete from {{ target }}
  where ({{ unique_key }}) in (
    select ({{ unique_key }})
    from {{ source }}
  );
  {% endif %}

  insert into {{ target }} ({{ dest_cols_csv }})
  (
    select {{ dest_cols_csv }}
    from {{ source }}
  )

{%- endmacro %}
