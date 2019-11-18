configure_file (
    "${PROJECT_SOURCE_DIR}/python/__init__.in.py"
    "${PROJECT_BINARY_DIR}/python/__init__.py"
)

add_python_module("orbf_v1" record.py onexit.py "${PROJECT_BINARY_DIR}/python/__init__.py")
