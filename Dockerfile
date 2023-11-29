FROM public.ecr.aws/lambda/python:3.10
#COPY . ${LAMBDA_TASK_ROOT}
RUN python -m pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt


ENV OPENAI_API_KEY="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"



CMD ["email_generator_lambda.app.handler"]
