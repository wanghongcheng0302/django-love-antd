import request from '@/utils/request';
import type { TableListParams, TableListItem } from './data.d';

// {[ model.label ]}查询
export async function query{[ model.name | capitalize ]}(params?: TableListParams) {
  return request('/api/backend/{[ app_name ]}/{[ model.name ]}/', {
    method: 'GET',
    params,
  });
}

// {[ model.label ]}创建
export async function create{[ model.name | capitalize ]}(data) {
  return request('/api/backend/{[ app_name ]}/{[ model.name ]}/', {
    method: 'POST',
    data,
  });
}

