from pyscript import document

dsp_missing_ppl = 0 

def submit_person_dsp(event):

    # Person submitted, increase total count of missing people
    dsp_missing_ppl += 1
    
    # Add a new row
    table = document.getElementById("DSPtable")
    dsp_name = document.getElementById("dsp-name").value
    dsp_reason = document.getElementById("dsp-reason").value

    row = table.insertRow(0)
    cell1 = row.insertCell(0)
    cell2 = row.insertCell(1)
    cell3 = row.insertCell(2)

    cell1.innerText = dsp_name #Name
    cell2.innerText = dsp_reason # Reason
    cell3 = document.CreateElement("INPUT") # Delete Button 
    cell3.setAttribute("type", "button")
    cell3.setAttribute("value","deleteMe")

    # return None