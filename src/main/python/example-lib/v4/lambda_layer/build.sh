#!/usr/bin/env sh

set -x
here=$(dirname "$(realpath "$0")")

build_path="${here}/build"
build_python_path="${build_path}/python"
dist_path="${here}/dist"

cd "${here}" || exit

mkdir -p "${build_python_path}" "${dist_path}"
pip install dist/*.whl -t build/python

cd "${build_python_path}" || exit
rm -rf ./*.dist-info ./*.egg-info
find . | grep __pycache__ | xargs rm -rf

cd "${build_path}" || exit
zip -r9 ../dist/package.zip ./*
