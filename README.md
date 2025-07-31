# python_xmla
Connecting to XMLA endpoint from Python.

Steps

1. I have provided the 5 Analysis Services DLLs below from a SQL Server 2019 installation. You may need to update these with DLLs for your particular XMLA endpoint's compatibility. 
    * Microsoft.AnalysisServices.AdomdClient.dll
    * Microsoft.AnalysisServices.Runtime.Core.dll
    * Microsoft.AnalysisServices.Runtime.Windows.dll
    * Microsoft.Identity.Client.dll
    * Microsoft.IdentityModel.Abstractions.dll
2. Upload these DLLs to a directory in a Unity Catalog volume.
3. Configure the notebook in the repository with your appropriate connection string for your XMLA endpoint, and the path of your UC volume directory from step 2.
4. **If Interactive**:
    * Open the web terminal on your cluster. Run the following command: ```sudo apt-get update && apt-get install -y dotnet-runtime``` and finish installation.
5. **If Automated**:
    * Add the command above to the init script of your cluster.

Post any issues here.
