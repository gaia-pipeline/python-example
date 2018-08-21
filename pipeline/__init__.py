from gaiasdk import sdk
import logging
import time

def CreateUser(args):
    logging.info("CreateUser has been started!")
    time.sleep(5)
    logging.info("CreateUser has been finished!")

def MigrateDB(args):
    logging.info("MigrateDB has been started!")
    time.sleep(5)
    logging.info("MigrateDB has been finished!")

def CreateNamespace(args):
    logging.info("CreateNamespace has been started!")
    time.sleep(5)
    logging.info("CreateNamespace has been finished!")

def CreateDeployment(args):
    logging.info("CreateDeployment has been started!")
    time.sleep(5)
    logging.info("CreateDeployment has been finished!")

def CreateService(args):
    logging.info("CreateService has been started!")
    time.sleep(5)
    logging.info("CreateService has been finished!")

def CreateIngress(args):
    logging.info("CreateIngress has been started!")
    time.sleep(5)
    logging.info("CreateIngress has been finished!")

def Cleanup(args):
    logging.info("Cleanup has been started!")
    time.sleep(5)
    logging.info("Cleanup has been finished!")

def main():
    logging.basicConfig(level=logging.INFO)
    createuser = sdk.Job("Create DB User", "Creates a database user with least privileged permissions.", CreateUser)
    migratedb = sdk.Job("DB Migration", "Imports newest test data dump and migrates to newest version.", MigrateDB, ["Create DB User"])
    createnamespace = sdk.Job("Create K8S Namespace", "Creates a new Kubernetes namespace for the new test environment.", CreateNamespace, ["DB Migration"])
    createdeployment = sdk.Job("Create K8S Deployment", "Creates a new Kubernetes deployment for the new test environment.", CreateDeployment, ["Create K8S Namespace"])
    createservice = sdk.Job("Create K8S Service", "Creates a new Kubernetes service for the new test environment.", CreateService, ["Create K8S Namespace"])
    createingress = sdk.Job("Create K8S Ingress", "Creates a new Kubernetes ingress for the new test environment.", CreateIngress, ["Create K8S Namespace"])
    cleanup = sdk.Job("Clean up", "Removes all temporary files.", Cleanup, ["Create K8S Deployment", "Create K8S Service", "Create K8S Ingress"])
    sdk.serve([createuser, migratedb, createnamespace, createdeployment, createservice, createingress, cleanup])
