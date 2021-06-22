import { InfoCircleOutlined } from '@ant-design/icons';
import { Button, Card, DatePicker, Input, Form, InputNumber, Radio, Select, Tooltip } from 'antd';
import type { Dispatch } from 'umi';
import { connect, FormattedMessage, formatMessage } from 'umi';
import type { FC } from 'react';
import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import styles from './style.less';
const FormItem = Form.Item;
const { Option } = Select;
const { RangePicker } = DatePicker;
const { TextArea } = Input;
interface BasicFormProps {
  submitting: boolean;
  dispatch: Dispatch;
}

{% for field in model.fields.values() %}
    {% if field.type in ["ForeignKey", "ManyToManyField"] %}
        import {  } from '@pages/{[ field.to.app_config.name ]}/{[ model.name ]}/service.ts'
    {% endif %}
{% endfor %}

const BasicForm: FC<BasicFormProps> = (props) => {
  const { submitting } = props;
  const [form] = Form.useForm();
  const [showPublicUsers, setShowPublicUsers] = React.useState(false);
  const formItemLayout = {
    labelCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 7,
      },
    },
    wrapperCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 12,
      },
      md: {
        span: 10,
      },
    },
  };
  const submitFormLayout = {
    wrapperCol: {
      xs: {
        span: 24,
        offset: 0,
      },
      sm: {
        span: 10,
        offset: 7,
      },
    },
  };

{#  外键、多对多类型的，通过接口生成Options，多对多支持多选，todo，前端的最佳做法是MVC分层，不采用ant design当下按模块分的方式  #}

  {%- for field in model.fields.values() %}
      {%- if field.type in ["ForeignKey", "ManyToManyField"] %}
          let {[ field.name ]}Options = []
      {% endif %}
  {%- endfor %}

  const onFinish = (values: Record<string, any>) => {
    const { dispatch } = props;
    dispatch({
      type: 'formAndbasicForm/submitRegularForm',
      payload: values,
    });
  };

  const onFinishFailed = (errorInfo: any) => {
    // eslint-disable-next-line no-console
    console.log('Failed:', errorInfo);
  };

  const onValuesChange = (changedValues: Record<string, any>) => {
    const { publicType } = changedValues;
    if (publicType) setShowPublicUsers(publicType === '2');
  };

  return (
    <PageContainer content="表单页用于向用户收集或验证信息，基础表单常见于数据项较少的表单场景。">
      <Card bordered={false}>
        <Form
          style={{
            marginTop: 8,
          }}
          form={form}
          name="basic"
          initialValues={{
            public: '1',
          }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          onValuesChange={onValuesChange}
        >
        {%- for field in model.fields.values() %}
            {%- if field.auto_now or field.auto_now_add or field.auto_created or field.is_primary_key %}
                {% continue %}
            {%- endif %}
        {%- if field.choices -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <Radio.Group>
            {%- for choice in field.choices %}
                <Radio value={ {[ choice.value ]} }>{[ choice.label ]}</Radio>
            {%- endfor %}
            </Radio.Group>
          </FormItem>
        {%- elif field.type in ['CharField', 'EmailField'] -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <Input placeholder="请输入{[ field.label ]}" />
          </FormItem>
        {%- elif field.type in ['BigAutoField', 'BigIntegerField', 'DecimalField', 'FloatField', 'IntegerField', 'PositiveBigIntegerField', 'PositiveIntegerField', 'PositiveSmallIntegerField', 'SmallIntegerField'] -%}
         <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <InputNumber />
          </FormItem>
        {%- elif field.type in ['DateField', 'DateTimeField', 'timefield',] -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <DatePicker  />
          </FormItem>
        {%- elif field.type in ['TextField', ] -%}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <TextArea showCount  />
          </FormItem>
        {%- elif field.type in ['ForeignKey', ] -%}
           <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
            >
            <Select defaultValue="lucy" style={{ width: 120 }} >
                <Option value="jack">Jack</Option>
            </Select>
          </FormItem>
        {%- elif field.type in ['ManyToManyField', ] %}
            <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={ [{
            {%- if field.blank -%}
                required: true,
            {%- endif -%}
                type: "{[ field.type | django_convert_typescript ]}",
            {%- if field.max_length -%}
                max: {[ field.max_length ]}
            {%- endif -%}}] }
          >
            <Select defaultValue="lucy" style={{ width: 120 }} >
                <Option value="jack">Jack</Option>
            </Select>
          </FormItem>
        {%- endif %}
        {% endfor %}
          <FormItem
            {...submitFormLayout}
            style={{ marginTop: 32 }}
          >
            <Button type="primary" htmlType="submit" loading={submitting}>
              提交
            </Button>
            <Button
              style={{
                marginLeft: 8,
              }}
            >
              保存
            </Button>
          </FormItem>
        </Form>
      </Card>
    </PageContainer>
  );
};

export default connect(
  ({
    loading,
  }: {
    loading: {
      effects: Record<string, boolean>;
    };
  }) => ({
    submitting: loading.effects['formAndbasicForm/submitRegularForm'],
  }),
)(BasicForm);
