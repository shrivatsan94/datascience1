pipeline{
    agent any
    
    stages{
      stage('checkout'){
        steps{
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/shrivatsan94/datascience1']]])
        }
    }
    
    stage('set environment'){
        steps{
            tool name: 'python3', type: 'jenkins.plugins.shiningpanda.tools.PythonInstallation'
        }
    }
    
    stage('python build'){
        steps{
            bat '''echo "command to build python code"'''
        }
    }
    
    stage('python lint'){
        steps{
            bat'''echo "command to execute lint"'''
        }
    }
    
    stage('python test'){
        steps{
            bat''' echo "command to execute test"'''
        }
    }
}

}