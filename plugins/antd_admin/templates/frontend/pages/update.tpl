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
          hideRequiredMark
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

        {% for field in model.fields.values() %}
        {# input #}
        {% if field.choices %}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={
            [{ required: true }]
            }
          >
            <Radio.Group>
            {% for choice in field.choices %}
                <Radio value={ {[ choice.value ]} }>{[ choice.label ]}</Radio>
            {% endfor %}

        </Radio.Group>
          </FormItem>

        {% elif field.type in ['CharField', 'EmailField'] %}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={
            [{ required: true }]
            }
          >
            <Input placeholder="请输入{[ field.label ]}" />
          </FormItem>

        {% elif not field.primary_key and field.type in ['BigAutoField', 'BigIntegerField', 'DecimalField', 'FloatField', 'IntegerField', 'PositiveBigIntegerField', 'PositiveIntegerField', 'PositiveSmallIntegerField', 'SmallIntegerField'] %}
         <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={
            [{ required: true }]
            }
          >
            <InputNumber />
          </FormItem>

        {% elif field.type in ['DateField', 'DateTimeField', 'timefield',] %}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={
            [{ required: true }]
            }
          >
            <DatePicker  />
          </FormItem>


        {% elif field.type in ['TextField', ] %}
        <FormItem
            {...formItemLayout}
            label={"{[ field.label ]}"}
            name="{[ field.name ]}"
            rules={
            [{ required: true }]
            }
          >
            <TextArea showCount  />
          </FormItem>

        {% elif field.type in ['ForeignKey', ] %}
        {% elif field.type in ['ManyToManyField', ] %}
        {% endif %}

        {% endfor %}
          <FormItem
            {...submitFormLayout}
            style={{
              marginTop: 32,
            }}
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
