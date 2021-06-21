// 字段
export type TableListItem = {
  {% for field in model.fields -%}
    {[ field.name ]}: {[ field.type | django_convert_typescript ]}
  {% endfor %}
};

// 分页参数
export type TableListPagination = {
  {[ pageConfig.totalParam ]}: number;
  {[ pageConfig.pageSizeParam ]}: number;
  {[ pageConfig.pageNumParam ]}: number;
};

// 数据
export type TableListData = {
  list: TableListItem[];
  pagination: Partial<TableListPagination>;
};

// 查询参数
export type TableListParams = {
  {[ pageConfig.search_param ]}?: string;
  {[ pageConfig.pageSizeParam ]}?: number;
  {[ pageConfig.pageNumParam ]}?: number;
  {% if model.list_filter -%}
  {% for field in model.list_filter -%}
  {% if enable_filter(field, model.fields)  -%}
  {[ field ]}?: any;
  {%- endif %}
  {%- endfor %}
  {%- endif %}
};


