#! /bin/sh

cm-authors > AUTHORS
git tag 
echo "New Tag?"; read TAG
git tag $TAG
echo $TAG
echo "__version__ = \"$TAG\"" > cloudmesh_client/version.py
git commit -m "version $TAG" cloudmesh_client/version.py
python setup.py install
git commit -m $TAG --allow-empty
git push origin --tags
git push
