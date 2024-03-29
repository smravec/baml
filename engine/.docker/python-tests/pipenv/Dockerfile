# Run a python test script
FROM python:3.8-slim

WORKDIR /myapp

# Install pipenv
RUN pip install pipenv

# Set up environment variables
ENV CAPTURE_DIR="/usr/src/logs"
ENV BAML_TEST_LOGS="/usr/src/logs/baml_test"
RUN mkdir -p /usr/src/logs

# Copy the test script into the image
COPY script.sh /usr/src/test.sh
RUN chmod +x /usr/src/test.sh

# Copy necessary files for your application
# Assuming you have a Pipfile and Pipfile.lock, copy them to the image to install dependencies
COPY Pipfile Pipfile.lock ./

# Install dependencies defined in Pipfile
RUN pipenv install --deploy --ignore-pipfile

# Copy the compiled binary from the builder stage, assuming baml is a separate binary
COPY --from=baml_builder /baml_source_code/target/release/baml /usr/tools/baml
ENV PATH="/usr/tools:${PATH}"

CMD ["/usr/src/test.sh"]
