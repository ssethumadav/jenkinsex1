groovy
CopyEdit
pipeline {
agent any
stages {
stage(&#39;Clone Repository&#39;) {
steps {
git &#39;https://https://github.com/ssethumadav/jenkinsex1.git;
}
}
stage(&#39;Install Dependencies&#39;) {
steps {
sh &#39;pip install -r requirements.txt&#39;
}
}
stage(&#39;Run Tests&#39;) {
steps {
sh &#39;pytest tests/&#39;
}
}
stage(&#39;Build Artifact&#39;) {
steps {
sh &#39;python setup.py sdist&#39;
}
}
stage(&#39;Archive Artifact&#39;) {
steps {
archiveArtifacts artifacts: &#39;dist/*.tar.gz&#39;, fingerprint:
true
}
}
}
}
